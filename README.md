# README

## Descrição
Este projeto consiste em dois algoritmos que realizam a busca em profundidade (DFS - Depth-First Search) em grafos direcionados, com variações para grafos onde os vértices são nomeados por números ou por letras.

### Arquivos Principais:
- `buscaEmProfundidade.py`: Algoritmo para grafos com vértices numerados por números.
- `buscaEmProfundidadeLetras.py`: Algoritmo para grafos com vértices nomeados por letras.

## Funcionalidades
- **DFS em Grafos com Vértices Numerados**
  - Para utilizar o algoritmo que lida com vértices numerados, execute o arquivo `buscaEmProfundidade.py`.
  - O algoritmo solicita o nome do arquivo `.txt` que contém a representação do grafo, onde os vértices são identificados por números.
  - O código lê o arquivo fornecido na mesma pasta e executa a DFS, exibindo informações sobre os tempos de descoberta e término, além de visualizar o grafo com as arestas coloridas de acordo com seu tipo.

- **DFS em Grafos com Vértices Nomeados por Letras**
  - Para utilizar o algoritmo que lida com vértices nomeados por letras, execute o arquivo `buscaEmProfundidadeLetras.py`.
  - Assim como no primeiro algoritmo, esse solicita o nome do arquivo `.txt` contendo a representação do grafo com vértices identificados por letras.
  - Após a execução, o código mostra informações sobre os tempos de descoberta e término, além de exibir o grafo com as arestas coloridas de acordo com seu tipo.

## Utilização
- Ao executar qualquer um dos algoritmos, o usuário deve fornecer o nome do arquivo `.txt` que descreve a estrutura do grafo desejado. Certifique-se de que o arquivo esteja na mesma pasta do código para evitar erros de leitura.

### Observações
- Caso ocorram erros ao abrir o arquivo `.txt`, verifique se o compilador está aberto na mesma pasta dos arquivos de código e dados.
- Foram disponibilizados arquivos de exemplo (`GD.txt` e `test.txt`) para testar os algoritmos com grafos numerados e nomeados por letras, respectivamente.

## Como Executar
Para executar os algoritmos:
1. Escolha o tipo de vértices (números ou letras) interagindo com a função `escolherFunção()`.
2. Siga as instruções para fornecer o nome do arquivo `.txt`.
3. Aguarde a execução e visualize os resultados.
