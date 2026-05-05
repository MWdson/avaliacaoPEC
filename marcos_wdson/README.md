# Descrção inicial
O script roda o sistema de uma biblioteca executando o CRUD para registro dos dados dos livros, via terminal é possivel inserir, editar, excluir e deletar os dados persistidos.
Os dados estão sendo salvos e sqlite3 que é uma biblioteca nativa do python pesente na maioria dos pacotes de instalação do Windows, Linux e Mac
## Execução
1. Clone o repositório: git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/MWdson/avaliacaoPEC.git)
2. Acesse a pasta de acordo com o nome do aluno
3. Execute o programa: python avaliacaopec.py
## Comparação
A implementação via função é mais simples contorle de manutenção futura, as funções tem apenas uma responsabilidade possibilitando identificar e tratar os erros de maneira mais simples, quando modularizados. Outro ponto que facilita é a modularização do código enquanto função.
A vantagem do código imperativo é o controle total de cada passo executado durante o script, porém pode ser um risco dependo do tamanho do código e da complexidade da funcionalidade.
Por pratica a abordagem funcional acaba se tornando mais facil para realizar a leitura do código.
Como mencionado acima o código quebrado em funções é de melhor legibilidade e mais facil de realizar manutenção.
## Tecnologias usadas
* python3
* sqlite3
* functools
