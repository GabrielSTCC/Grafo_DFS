def inicializar_DFS_NUM():
    import networkx as nx
    import matplotlib.pyplot as plt
    
    def imprime_Num(d, f, N):
        print("\n Tempo de Descorberta e tempo que ficou Preta:")
        
        for i in range(N):
            print("Vértiece ", i+1, ":", d[i], f[i])
        
    def desenhar_grafo(lista_adj, tipo_aresta):
        G = nx.DiGraph()  # Cria um grafo direcionado
        for u, vizinhos in enumerate(lista_adj):
            G.add_node(u + 1)  # Adiciona vértices numerados a partir de 1

            for v in vizinhos:
                tipo_aresta_ = tipo_aresta[(u, v)] 
                G.add_edge(u + 1, v + 1, color=tipo_aresta_)  # Adiciona arestas direcionadas considerando o offset de 1 e atribui o tipo de aresta

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
            
    def sequencia(lista_adj, N):
        def encontraMaiorGrau(grafo):
            maior_vertice = None    
            maior_grau = -1
            for i, vizinhos in enumerate(grafo):
                grau_saida = len(vizinhos)
                if grau_saida > maior_grau:
                    maior_grau = grau_saida
                    maior_vertice = i
            return maior_vertice

        # Encontrar vértice com o maior grau de saída
        vertice_inicial = encontraMaiorGrau(lista_adj)
        
        # Lista para armazenar a sequência de vértices
        sequencia_resultante = []

        # Inicialmente, adiciona o vértice de maior grau de saída à sequência
        sequencia_resultante.append(vertice_inicial)

        # Marcar o vértice inicial como visitado
        visitados = [False] * N
        visitados[vertice_inicial] = True

        # Percorrer os vértices a partir do vértice inicial para formar a sequência
        fila = [vertice_inicial]
        while fila:
            u = fila.pop(0)
            for v in lista_adj[u]:
                if not visitados[v]:
                    visitados[v] = True
                    sequencia_resultante.append(v)
                    fila.append(v)

        return sequencia_resultante
        


    def loadLista_Num(nomeDoAqruivo):
        documento = nomeDoAqruivo + '.txt'
        arquivo = open(documento, 'r')
        lista = arquivo.readlines() #Ler todas as linhas e salvar
        for i in range(len(lista)):
            linha = lista[i].split()
            if i == 0:
                N = int (linha[0])
                lista_adj = [[] for _ in range(N)]  
            else:
                lista_adj[int(linha[0]) - 1].append(int(linha[1])-1)
        arquivo.close()
        return lista_adj, N


                
    def DFS_Visit_Num(u, lista_adj, tipo_aresta):
        global mark
        cor[u] = "Cinza"
        mark = mark + 1
        d[u] = mark
        
        for v in lista_adj[u]:
            if cor[v] == "Branco":
                tipo_aresta[(u, v)] = "Arvore"
                print("Aresta (", u+1,"-",v+1, "): Arvore")
                DFS_Visit_Num(v, lista_adj, tipo_aresta)
            elif cor[v] == "Cinza":
                tipo_aresta[(u, v)] = "Retorno"
                print("Aresta (", u+1,"-",v+1, "): Retorno")
            elif cor[v] == "Preto" and d[u] < d[v]:
                tipo_aresta[(u, v)] = "Avanco"
                print("Aresta (", u+1,"-",v+1, "): Avanço")
            else:
                tipo_aresta[(u, v)] = "Cruzamento"
                print("Aresta (", u+1,"-",v+1, "): Cruzamento")
        cor[u] = "Preto"
        mark = mark + 1
        f[u] = mark
        
    def DFS_Num():
        print(" Tipo das Arestas:")
        for u in V:
            cor[u] = "Branco"
        for u in V:
            if cor[u] == "Branco":
                DFS_Visit_Num(u, lista_adj, tipo_aresta)
                
    print("Qual o nome do arquivo que voce deseja?")
    nomeDoAquivo = input()
    [lista_adj, N] = loadLista_Num(nomeDoAquivo)  
    V = sequencia(lista_adj, N)
    cor = [0]*N
    d = [0]*N
    f = [0]*N
    global mark
    mark = 0
    tipo_aresta = {}
    DFS_Num()
    imprime_Num(d,f,N)
    desenhar_grafo(lista_adj, tipo_aresta)
#inicializar_DFS_NUM()
    
