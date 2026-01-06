from comuns import matriz_tuplo, get_neighbors, GOAL, MAX_LIMT

# Funções para os algoritmos BFS e DFS
#matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]

# Modificar para funcionar com as matrizes
def bfs(matriz_init, limite):
    init = matriz_tuplo(matriz_init)
    fim = GOAL
    
    visitados = set()
    gerados = []
    expandidos = []
    
    fila = [init]
    gerados.append(init)
    
    contador = 0
    while fila:
        node = fila.pop(0)
        contador+=1
        
        print(f"DEBUG -- Tentativa num: {contador}")
        
        if node not in visitados:
            visitados.add(node)
            expandidos.append(node)
            
            if node == fim:
                print(f"O || BFS || resolveu o tabuleiro em {contador} tentativas")
                return True, gerados, expandidos
            
            for vizi in get_neighbors(node):
                if vizi not in visitados and vizi not in fila:
                    fila.append(vizi)
                    gerados.append(vizi)
                    
        if contador == limite:
            print(f"O || BFS || não resolveu o tabuleiro em {contador} tentativas")
            return False
        
        elif contador == MAX_LIMT:
            print(f"O || BFS || não resolveu o tabuleiro em {contador} tentativas")
            return False
        
                
    return False, gerados, expandidos


# Modificar para funcionar com as matrizes
def dfs(matriz_init,limite):
    
    init = matriz_tuplo(matriz_init)
    fim = GOAL
    
    visitados = set()
    gerados = []
    expandidos = []
    
    pilha = [init]
    gerados.append(init)
    contador = 0
    while pilha:
        node = pilha.pop()
        contador +=1
        
        print(f"DEBUG -- Tentativa num: {contador}")
        
        
        if node not in visitados:
            visitados.add(node)
            expandidos.append(node)
            
            if node == fim:
                print(f"O || DFS || resolveu o tabuleiro em {contador} tentativas")                
                return True, gerados, expandidos
            
            for vizi in reversed(get_neighbors(node)):
                if vizi not in visitados and vizi not in pilha:
                    pilha.append(vizi)
                    gerados.append(vizi)
        
        if contador == limite:
            print(f"O || BFS || não resolveu o tabuleiro em {contador} tentativas")
            return False
        
        elif contador == MAX_LIMT:
            print(f"O || BFS || não resolveu o tabuleiro em {contador} tentativas")
            return False
        
        
    return False, gerados, expandidos

if __name__ == "__main__":
    bfs(matriz_jogo_quinze,-1)
    #dfs(matriz_jogo_quinze)
    