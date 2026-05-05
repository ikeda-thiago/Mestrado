import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from devito import (Grid, TimeFunction, Function, Eq, Operator,
                    configuration, SubDomain, solve)

from devito.petsc import petscsolve, EssentialBC
from devito.petsc.initialize import PetscInitialize
configuration['compiler'] = 'custom'
os.environ['CC'] = 'mpicc'

# Subdomains to implement BCs
class SubTop(SubDomain):
    name = 'subtop'

    def define(self, dimensions):
        x, y = dimensions
        return {x: x, y: ('right', 1)}


class SubBottom(SubDomain):
    name = 'subbottom'

    def define(self, dimensions):
        x, y = dimensions
        return {x: x, y: ('left', 1)}


class SubLeft(SubDomain):
    name = 'subleft'

    def define(self, dimensions):
        x, y = dimensions
        return {x: ('left', 1), y: ('middle', 1, 1)}


class SubRight(SubDomain):
    name = 'subright'

    def define(self, dimensions):
        x, y = dimensions
        return {x: ('right', 1), y: ('middle', 1, 1)}


sub1 = SubTop()
sub2 = SubBottom()
sub3 = SubLeft()
sub4 = SubRight()

subdomains = (sub1, sub2, sub3, sub4)


def analytical(x, y):
    return np.float64(np.exp(x-y) * x * (1-x) * y * (1-y))


Lx = np.float64(1.)
Ly = np.float64(1.)

n_values = list([11, 21])
dX = np.array([Lx/(n-1) for n in n_values])
dy = np.array([Ly/(n-1) for n in n_values])
errors = []

tstop = 1
sigma = 0.1
dt = np.array([sigma * dx * dy for dx, dy in zip(dX, dy)])
nt_values = np.round(tstop / dt).astype(int)
for n in n_values:

    grid = Grid(shape=(n, n), extent=(Lx, Ly), subdomains=subdomains, dtype=np.float64)

    phi = TimeFunction(name='phi', grid=grid, space_order=2, dtype=np.float64)
    rhs = Function(name='rhs', grid=grid, space_order=2, dtype=np.float64)
    bc = Function(name='bc', grid=grid, space_order=2, dtype=np.float64)

    phi.data[:] = 0.0

    tmpx = np.linspace(0, Lx, n).astype(np.float64)
    tmpy = np.linspace(0, Ly, n).astype(np.float64)
    Y, X = np.meshgrid(tmpx, tmpy)

    rhs.data[:] = np.float64(
        2.0*X*(Y-1.0)*(Y - 2.0*X + X*Y + 2.0)
    ) * np.float64(np.exp(X-Y))

    eqn = Eq(phi.laplace, rhs, subdomain=grid.interior)
    stencil = solve(eqn, phi)
    eq_stencil = Eq(phi, stencil, subdomain=grid.interior)
    bc.data[:] = 0.0

    # # Create boundary condition expressions using subdomains
    bcs = [EssentialBC(phi, bc, subdomain=sub1)]
    bcs += [EssentialBC(phi, bc, subdomain=sub2)]
    bcs += [EssentialBC(phi, bc, subdomain=sub3)]
    bcs += [EssentialBC(phi, bc, subdomain=sub4)]

    exprs = [eqn] + bcs
    #petsc = petscsolve(exprs, target=phi, solver_parameters={'ksp_rtol': 1e-10})

    op = Operator([eq_stencil] + bcs)
    op(time_m=0, time_M=nt_values[n_values.index(n)], dt=dt[n_values.index(n)])

    phi_analytical = analytical(X, Y)

    error = np.sqrt(np.sum((phi_analytical - phi.data[0])**2)) / np.sqrt(np.sum(phi_analytical**2))
    errors.append(error)
    print(f'Iteration = {nt_values[n_values.index(n)]}')

    if n == 11:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X.flatten(), Y.flatten(), phi.data[0].flatten(), c='r', marker='o', label='Solução Devito')
        ax.plot_surface(X, Y, phi_analytical, cmap='viridis', alpha=0.5, label='Solução Analítica')
        ax.set_xlabel(r'x')
        ax.set_ylabel(r'y')
        ax.set_zlabel(r'P(x,y)')
        plt.legend()
        plt.savefig(fname=f'{n}_devito.png', dpi=500)

slope, _ = np.polyfit(np.log(dX), np.log(errors), 1)

#assert slope > 1.9
#assert slope < 2.1
print(f"Errors: {errors}")
print(f"Convergence rate: {slope:.5f}")

convergence_rates = []
for i in range(len(errors) - 1):
    rate = (np.log(errors[i+1]) - np.log(errors[i])) / (np.log(dX[i+1]) - np.log(dX[i]))
    convergence_rates.append(rate)
print(f"Convergence rates between successive grid refinements: {convergence_rates}")