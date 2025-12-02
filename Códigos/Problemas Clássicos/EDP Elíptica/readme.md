<h1 align="center"> EDP Elíptica </h1>

Equações diferenciais parciais elípticas representam uma classe fundamental de problemas na física matemática e engenharia, caracterizando fenômenos em estado estacionário cujos efeitos se propagam instantaneamente em todas as direções. A Equação de Poisson constitui o exemplo paradigmático deste tipo de equação.

Nessa seção, aborda-se a resolução numérica da Equação de Poisson utilizando o Devito, com ênfase na validação da precisão numérica mediante comparação com soluções analíticas. A estratégia de soluções manufaturadas é empregada, permitindo a quantificação precisa dos erros de discretização. Serão considerados problemas bidimensionais e tridimensionais em geometrias regulares, com condições de contorno de Dirichlet.

O método de diferenças finitas é utilizado para a discretização espacial, enquanto a técnica de *pseudo-timestepping* é empregada para contornar a limitação do Devito em resolver sistemas lineares implicitamente, transformando o problema elíptico estacionário em um problema parabólico transiente fictício até a convergência para o estado estacionário.
