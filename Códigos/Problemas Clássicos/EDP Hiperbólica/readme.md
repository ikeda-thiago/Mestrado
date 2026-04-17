O enfoque é direcionado à aplicação do Devito na resolução de equações diferenciais parciais (EDPs) de natureza hiperbólica. Tais equações caracterizam-se pela propagação de informações ao longo de características, sendo particularmente relevantes para modelar fenômenos de transporte e propagação de ondas. Um aspecto fundamental das EDPs hiperbólicas é sua capacidade de desenvolver e propagar descontinuidades, mesmo a partir de condições iniciais suaves.

O principal desafio numérico nesse contexto reside no controle de erros de discretização, que se manifestam principalmente como:

\begin{itemize}
\item[\color{blue}$\blacktriangleright$] \textbf{dissipação numérica:} amortecimento não físico dos gradientes da solução;
\item[\color{blue}$\blacktriangleright$] \textbf{dispersão numérica:} surgimento de oscilações espúrias em regiões de grandes gradientes.
\end{itemize}


Serão analisados dois casos distintos: um problema unidimensional e um problema bidimensional. A abordagem numérica adotará o esquema \textit{upwind} de primeira ordem implementado no Devito, com validação por meio de comparações com implementações equivalentes em NumPy e com a solução analítica.
