
A equação de difusão representa um dos modelos mais fundamentais na física matemática, descrevendo fenômenos de transporte de massa, calor ou outras grandezas através de meios materiais. Nesta seção, aborda-se a equação de difusão bidimensional na forma:

$$ \dfrac{\partial T}{\partial t} - \nu \dfrac{\partial ^2 T}{\partial x^2} - \nu \dfrac{\partial ^2 T}{\partial y^2} =  f, $$

em que $T(t, x, y)$ representa o transporte de calor ($^\text{o}C$), $\nu$ o coeficiente de difusidade térmica ($m^2/s$) e $f$ o termo fonte ($^\text{o}C/s$) que modela uma fonte ou sumidouro de calor em um domínio $\Omega_1 = [0,1]\times [0,1]$ ou $\Omega_2 = [0,2\pi]\times[0,2\pi]$.

A correta discretização do termo fonte é crucial para a precisão numérica de esquemas de diferenças finitas. Diferentes formulações do termo fonte podem representar desde casos simples com geração uniforme até situações complexas com dependência espacial e temporal.

O objetivo principal desta seção é demonstrar a flexibilidade do Devito na implementação de termos fonte com complexidade crescente, seguindo uma progressão pedagógica que inclui:

* Termo fonte constante: caso mais elementar, representando geração uniforme em todo o domínio;
* Termo fonte espacialmente dependente: variação unidimensional ao longo de uma direção espacial;
* Termo fonte bidimensional: variação completa no espaço bidimensional;
* Termo fonte espaço-temporal: dependência temporal combinada com variação espacial unidimensional;
* Termo fonte completo: caso mais geral com dependência temporal e espacial completa.

Através desta abordagem progressiva, busca-se não apenas ilustrar as capacidades do Devito para tratar problemas com diferentes níveis de complexidade, mas também fornecer um roteiro para a implementação de termos fonte arbitrários em problemas de equações diferenciais parciais. A análise comparativa das soluções numéricas para cada caso permitirá avaliar a influência do termo fonte no comportamento da solução e verificar a correta implementação no Devito.

Para as simulações numéricas, considera-se $\Delta t = \dfrac{\Delta x \Delta y}{4\nu}$ e tempo final de $1$ segundo.
