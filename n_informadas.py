from comuns import matriz_tuplo, get_neighbors, GOALS, MAX_LIMIT
# Funções para os algoritmos BFS e DFS

def bfs(matriz_init, limite, tipo_goal):
    init = matriz_tuplo(matriz_init)
    fim = GOALS[tipo_goal]
    
    visitados = set()
    gerados = []
    expandidos = []
    
    fila = [init]
    gerados.append(init)
    
    contador = 0
    while fila:
        node = fila.pop(0)
        contador+=1
        
        if contador % 10000 == 0: 
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
        
        elif contador == MAX_LIMIT:
            print(f"O || BFS || não resolveu o tabuleiro em {contador} tentativas -- LIMITE ACIONADO")
            return False
        
                
    return False, gerados, expandidos


# Modificar para funcionar com as matrizes
def dfs(matriz_init,limite, tipo_goal):
    
    init = matriz_tuplo(matriz_init)
    fim = GOALS[tipo_goal]
    
    visitados = set()
    gerados = []
    expandidos = []
    
    pilha = [init]
    gerados.append(init)
    contador = 0
    while pilha:
        node = pilha.pop()
        contador +=1
        
        if contador % 10000 == 0:
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
        
        elif contador == MAX_LIMIT:
            print(f"O || BFS || não resolveu o tabuleiro em {contador} tentativas")
            return False
        
        
    return False, gerados, expandidos
