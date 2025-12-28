import heapq
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


def dist_manhatan(matriz_tabuleiro, matriz_goal): # Distância da posição atual do quadrado para a posição onde este é suposto estar
    dist = 0
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = matriz_tuplo(matriz_goal)
    
    for i, quadrado in enumerate(tabuleiro):
        if quadrado == 0:
            continue
        
        fila, coluna = divmod(i,4) # Posição do quadrado atual
        
        goal_fila, goal_coluna = divmod(goal.index(quadrado), 4) # Posição suposta do quadrado

        dist += abs(fila - goal_fila) + abs(coluna - goal_coluna) # Calcular a distância em si

        # DEBUG        
        # print(f"DEBUG -- O quadrado {quadrado} está na posição: x = {fila} | y = {coluna}") 
        # print(f"DEBUG -- O objetivo está na posição: x = {goal_fila} | y = {goal_coluna}") 
        # print(f"DEBUG -- Distância entre o quadrado {goal_fila} e {goal_coluna}: {dist}") 
        

def unc(matriz_tabuleiro, matriz_goal):
    fila = []
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = matriz_tuplo(matriz_goal)
    
    heapq.heappush(fila, (0, tabuleiro))
    
    visitados = {}
    contador = 0
    
    while fila:
        custo, node = heapq.heappop(fila)
        contador += 1
        #print(f"DEBUG -- Custo atual: {custo} | Nó atual: {node}")
        
        if node in visitados and visitados[node] <= custo:
            continue
        
        visitados[node] = custo
        
        if node == goal:
            print(f"O UFS resolveu o tabuleiro em {contador} tentativas com um custo total de {custo}.")
            return True
        
        for vizi in get_neighbors(node):
            heapq.heappush(fila, (custo + 1, vizi))
    
    return False
        
if __name__ == "__main__":
    # dist_manhatan(matriz_jogo_quinze, matriz_goal)

    unc(matriz_jogo_quinze, matriz_goal)