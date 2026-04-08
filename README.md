# Dissertação de Mestrado

## Códigos da Dissertação: Explorando Devito: uma Abordagem para Otimizar a Resolução de Escoamentos Viscosos por Diferenças Finitas

Este repositório contém todos os códigos desenvolvidos para a minha dissertação de Mestrado em Matemática Aplicada e Computacional, sob orientação da Profª. Drª. Gilcilene Sanchez de Paulo.


## Resumo

O estudo e a resolução de problemas modelados por equações diferenciais desempenham um papel fundamental na ciência e engenharia. A técnica de diferenças finitas é uma abordagem comum para resolver equações diferenciais ordinárias e parciais, porém sua implementação manual pode ser trabalhosa e suscetível a erros. Neste contexto surge o Devito, uma ferramenta de código aberto desenvolvida em Python que automatiza a geração e otimização de códigos de diferenças finitas, originalmente criada para aplicações sísmicas mas já testada com sucesso em problemas clássicos de CFD.

Este trabalho inicia com a implementação de problemas modelados por EDPs clássicas (parabólicas, hiperbólicas e elípticas) no Devito, servindo como fundamentação para o desenvolvimento posterior. Em seguida, o foco principal é a implementação da formulação corrente-vorticidade (ψ-ω) para as equações de Navier-Stokes, aplicada ao problema da cavidade *lid-driven*. Esta estratégia visa contornar limitações da formulação atual do Devito, que baseia o cálculo da pressão em uma equação de Poisson sem condição de contorno natural fisicamente aceitável.

Os resultados numéricos obtidos, embora satisfatórios, apontam algumas limitações da formulação atual no Devito, como o uso exclusivo de métodos explícitos (Jacobi) para solução da equação de Poisson. Este trabalho demonstra que o Devito é uma ferramenta promissora e em construção, cujas limitações podem ser superadas com contribuições de pesquisadores, abrindo caminhos para futuras aplicações em escoamentos de fluidos não-Newtonianos.
