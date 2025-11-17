matriz_jogo_oito = [[2,4,5],[3,6,7],[1,8,0]]
matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]

def show_state(matriz):
    print(f"Estado atual da matriz")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()
    print("\n")

# Modificar para funcionar com as matrizes
# AAFAFASFA
def bfs(grafo, init, fim):
    visitados = []
    gerados = []
    expandidos = []
    
    caminho = [init]
    gerados.append(init)
    
    while caminho:
        node = caminho.pop(0)
        if node not in visitados:
            visitados.append(node)
            expandidos.append(node)
            
            if node == fim:
                break
            
            for vizi in grafo[node]:
                if vizi not in visitados and vizi not in caminho:
                    caminho.append(vizi)
                    gerados.append(vizi)

# Modificar para funcionar com as matrizes
def dfs(grafo, init, fim):
    visitados = []
    gerados = []
    expandidos = []
    
    caminho = [init]
    gerados.append(init)
    
    while caminho:
        node = caminho.pop()
        if node not in visitados:
            visitados.append(node)
            expandidos.append(node)
            
            if node == fim:
                break
            
            for vizi in reversed(grafo[node]):
                if vizi not in visitados and vizi not in caminho:
                    caminho.append(vizi)
                    gerados.append(vizi)


#show_state(matriz_jogo_oito)

show_state(matriz_jogo_quinze)