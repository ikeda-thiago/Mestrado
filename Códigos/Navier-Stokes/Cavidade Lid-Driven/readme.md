<h1 align="center"> Problema da Cavidade Lid-Driven </h1>

As Equações de Navier-Stokes representam o pilar fundamental da mecânica dos fluidos newtonianos. Estas equações descrevem a conservação de massa, quantidade de movimento e energia para fluidos viscosos incompressíveis, constituindo um sistema acoplado de equações diferenciais parciais não-lineares. 

Nesse capítulo, aborda-se a implementação numérica das equações de Navier-Stokes utilizando o Devito, com ênfase em uma configuração clássica da dinâmica dos fluidos computacional: o escoamento em cavidade lid-driven. Problema esse consolidado na literatura, permitindo a avaliação da capacidade do Devito em capturar fenômenos fluidodinâmicos complexos.

O objetivo central é demonstrar a aplicabilidade do Devito na simulação de escoamentos viscosos incompressíveis, avaliando sua precisão na reprodução de estruturas vorticais, perfis de velocidade e corrente. Através de comparações com resultados numéricos e experimentais da literatura, busca-se estabelecer os limites e potencialidades dessa ferramenta no contexto da dinâmica dos fluidos computacional.

Utiliza-se a formulação corrente-vorticidade para as equações de Navier-Stokes, obtendo as seguintes equações:

$$
\frac{\partial \omega}{\partial t} + u \frac{\partial \omega}{\partial x} + v \frac{\partial \omega}{\partial y} = \frac{1}{Re} \left( \frac{\partial^2 \omega}{\partial x^2} + \frac{\partial^2 \omega}{\partial y^2} \right)
$$

$$
\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2} = -\omega
$$

$$
u = \frac{\partial \psi}{\partial y}, \qquad v = -\frac{\partial \psi}{\partial x}
$$

$$
w = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}
$$
