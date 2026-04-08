# Dissertação de Mestrado

## Códigos da Dissertação: Explorando Devito: uma Abordagem para Otimizar a Resolução de Escoamentos Viscosos por Diferenças Finitas

Este repositório contém todos os códigos desenvolvidos para a minha dissertação de Mestrado em Matemática Aplicada e Computacional, sob orientação da Profª. Drª. Gilcilene Sanchez de Paulo.


## Introdução
O estudo e a resolução de problemas modelados por equações diferenciais desempenham um papel fundamental em diversas áreas da ciência e engenharia. A técnica de diferenças finitas é uma abordagem comum para resolver equações diferenciais ordinárias (EDOs) e parciais (EDPs), envolvendo a discretização do domínio do problema e a aproximação por meio de equações de diferenças para calcular as derivadas das funções no espaço e no tempo.

Embora eficaz, a implementação manual de códigos de diferenças finitas pode ser trabalhosa, suscetível a erros e exigir um conhecimento técnico substancial de programação sofisticada. Outro ponto importante a ser considerado nesta área é a complexidade dos problemas numéricos de grande porte e com riqueza de detalhes a serem resolvidos atualmente. Essas simulações consomem uma quantidade significativa de recursos computacionais e tempo de processamento, muitas vezes exigindo supercomputadores para serem concluídas em um prazo razoável, o que torna esses problemas desafiadores em termos de escalabilidade e eficiência computacional.

Neste contexto, surge o Devito, uma ferramenta de código aberto desenvolvida em Python\texttrademark, projetada para automatizar a geração e otimização de códigos de diferenças finitas \cite{devito-api, devito-compiler}. O Devito foi originalmente desenvolvido para resolver aplicações sísmicas, incluindo a propagação de ondas sísmicas em diferentes tipos de materiais geológicos. Porém, o \textit{framework} também foi testado para resolver problemas clássicos de CFD, demonstrando sua flexibilidade em outros domínios de aplicação, como a equação de convecção, a equação de Burgers, a equação de Poisson, a equação de águas rasas, a equação de Darcy, bem como uma formulação inicial para as equações de Navier-Stokes que resolve o problema da cavidade.

Para compreender na prática o funcionamento do Devito, este trabalho inicia com a implementação de problemas modelados por EDPs clássicas - parabólicas, hiperbólicas e elípticas - servindo como fundamentação para o desenvolvimento posterior. Adicionalmente, são incluídas verificações de precisão numérica mediante a utilização de soluções manufaturadas, o que demandou também o aprendizado da implementação de termos fonte de forma otimizada no Devito.


A formulação para resolver as equações de Navier-Stokes atualmente implementada no Devito baseia-se no cálculo da pressão por meio de uma equação de Poisson que, na maioria dos problemas, não admite uma condição de contorno natural fisicamente aceitável. Neste tipo de formulação, tal condição de contorno requer sempre muita atenção.

Nesta direção, surge este estudo que visa a implementação de uma estratégia sólida, baseada na formulação corrente-vorticidade ($\psi - \omega$) \cite{Fromm1964}, a fim de aproveitar todas as potencialidades e vantagens do Devito no campo das soluções numéricas para escoamentos viscosos, com vistas à futura ampliação para outras formulações e escoamentos de fluidos não-Newtonianos, reologicamente mais complexos.

%Adicionalmente, esta formulação é bastante viável para ser implementada em uma nova ferramenta como o Devito durante um Mestrado, oferecendo possibilidades de explorá-lo ao máximo quanto às suas potencialidades e limitações, o que abre caminhos para extensões e aprofundamento da pesquisa do grupo SoMMa (Soluções de Modelos Matemáticos).

Muitas das potencialidades do Devito já foram descritas até aqui. Quanto às limitações, pode-se considerar o fato de que o Devito utiliza, por enquanto, apenas métodos explícitos para solução da equação de Poisson, como o método de Jacobi. Sabe-se da teoria de métodos numéricos para a equação de Poisson que o método de Jacobi é computacionalmente lento. Esta limitação também justifica o presente estudo, pois demonstra que o Devito é uma ferramenta atual, em construção, cujas limitações podem ser superadas com as contribuições de pesquisadores e desenvolvedores.

Este trabalho está organizado em cinco capítulos. O Capítulo 2 apresenta os conceitos básicos do Devito, incluindo sua \textit{API}, definição de domínios, funções e derivadas. O Capítulo 3 aborda a implementação de problemas clássicos com EDPs elípticas, hiperbólicas e parabólicas, essencial para validar a metodologia e familiarizar-se com a ferramenta. %O Capítulo 4 detalha a implementação da formulação corrente-vorticidade para as equações de Navier-Stokes, aplicada ao problema da cavidade \textit{lid-driven}, justificando-se pela necessidade de contornar limitações da formulação atual no Devito. 
O Capítulo 4 detalha a implementação da formulação corrente-vorticidade para as equações de Navier-Stokes, aplicada ao problema da cavidade \textit{lid-driven}. Os resultados numéricos obtidos, embora satisfatórios, apontam algumas limitações da formulação atual no Devito. O Capítulo 5, por fim, apresenta as perspectivas para as próximas etapas desse trabalho.
