# Funções para os algoritmos BFS e DFS

#matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]
matriz_goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,0]]


def matriz_tuplo(matriz):
    return tuple(num for row in matriz for num in row)

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 4)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            new_zero = nr * 4 + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))

    return neighbors


# Modificar para funcionar com as matrizes
def bfs(matriz_init, matriz_fim):
    init = matriz_tuplo(matriz_init)
    fim = matriz_tuplo(matriz_fim)
    
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
                print(f"O tabuleiro foi resolvido pelo BFS em {contador} tentativas")
                return True, gerados, expandidos
            
            for vizi in get_neighbors(node):
                if vizi not in visitados and vizi not in fila:
                    fila.append(vizi)
                    gerados.append(vizi)
    
    return False, gerados, expandidos


# Modificar para funcionar com as matrizes
def dfs(matriz_init, matriz_fim):
    
    init = matriz_tuplo(matriz_init)
    fim = matriz_tuplo(matriz_fim)
    
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
                print(f"O tabuleiro foi resolvido pelo BFS em {contador} tentativas")                
                return True, gerados, expandidos
            
            for vizi in reversed(get_neighbors(node)):
                if vizi not in visitados and vizi not in pilha:
                    pilha.append(vizi)
                    gerados.append(vizi)

    return False, gerados, expandidos

if __name__ == "__main__":
    bfs(matriz_jogo_quinze, matriz_goal)
    #dfs(matriz_jogo_quinze, matriz_goal)
    