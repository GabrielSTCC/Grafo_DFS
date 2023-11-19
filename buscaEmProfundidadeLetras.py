def inicializar_DFS_LETRA():
    import networkx as nx
    import matplotlib.pyplot as plt
    
    def imprime_Letra(d, f):
        print("\n Tempo de Descorberta e tempo que ficou Preta:")
        for vertice in d:
            print(f"Vértice {vertice}: {d[vertice]}, {f[vertice]}")
            
    def desenhar_grafo(lista_adj, tipo_aresta):
        G = nx.DiGraph()  # Cria um grafo direcionado

        for u, vizinhos in lista_adj.items():
            G.add_node(u)  # Adiciona vértices com nomes de letras

            for v in vizinhos:
                tipo_aresta_ = tipo_aresta[(u, v)]
                G.add_edge(u, v, color=tipo_aresta_)  # Adiciona arestas direcionadas e atribui o tipo de aresta

        pos = nx.spring_layout(G)
        cores_arestas = {'Arvore': 'blue', 'Avanco': 'yellow', 'Cruzamento': 'red', 'Retorno': 'pink'}

        edge_colors = []
        for u, v, d in G.edges(data=True):
            tipo_aresta_ = d['color']
            cor = cores_arestas[tipo_aresta_]
            edge_colors.append(cor)

        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', arrows=True, edge_color=edge_colors, width=2)  # Define as cores das arestas e suas larguras

        plt.title('Grafo Direcionado com Cores de Arestas')
        plt.show()

    def DFS_Visit_Letra(u, lista_adj, tipo_aresta):
        cor[u] = "Cinza"
        mark[0] += 1
        d[u] = mark[0]
        if u in lista_adj:
            for v in lista_adj[u]:
                if cor[v] == "Branco":
                    tipo_aresta[(u, v)] = "Arvore"
                    print(f"Aresta ({u} - {v}): Arvore")
                    DFS_Visit_Letra(v, lista_adj, tipo_aresta)
                elif cor[v] == "Cinza":
                    tipo_aresta[(u, v)] = "Retorno"
                    print(f"Aresta ({u} - {v}): Retorno")
                elif cor[v] == "Preto" and d[u] < d[v]:
                    tipo_aresta[(u, v)] = "Avanco"
                    print(f"Aresta ({u} - {v}): Avanço")
                else:
                    tipo_aresta[(u, v)] = "Cruzamento"
                    print(f"Aresta ({u} - {v}): Cruzamento")
        cor[u] = "Preto"
        mark[0] += 1
        f[u] = mark[0]

    def loadLista_Letra(nomeDoArquivo):
        documento = nomeDoArquivo + '.txt'
        arquivo = open(documento, 'r')
        dados = arquivo.readlines()
        lista = {}
        for i in range(1, len(dados)):
            linha = dados[i].split()
            u = linha[0]
            v = linha[1]
            if u not in lista:
                lista[u] = []
            lista[u].append(v)
        arquivo.close()
        return lista

    def DFS_Letra():
        print(" Tipo das Arestas:")
        for u in lista.keys():
            cor[u] = "Branco"
            d[u] = None # Inicializando o tempo de descoberta para o vértice u como None
            f[u] = None # Inicializando o tempo de finalização para o vértice u como None
        for u in lista.keys():
            if cor[u] == "Branco":
                DFS_Visit_Letra(u, lista, tipo_aresta)
        imprime_Letra(d, f)
    print("Qual o nome do arquivo que você deseja?")
    lista = loadLista_Letra(input())
    cor = {}
    d = {}
    f = {}
    mark = [0]
    tipo_aresta = {}
    DFS_Letra()

    desenhar_grafo(lista, tipo_aresta)
    
#inicializar_DFS_LETRA()
