import heapq
from comuns import matriz_tuplo, get_neighbors

#matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
matriz_jogo_quinze = [[1,2,3,4], [5,6,7,8], [9,14,10,12], [0,13,11,15]]
#matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]

matriz_goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,0]]



def dist_manhatan(tabuleiro, goal): # Distância da posição atual do quadrado para a posição onde este é suposto estar
    dist = 0
    
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
    
    return dist
        

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


def astar(matriz_tabuleiro, matriz_goal):
    fila = []
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = matriz_tuplo(matriz_goal)
    
    heapq.heappush(fila, (dist_manhatan(tabuleiro, goal),0,tabuleiro))
    
    visitados = {}
    contador = 0
    
    while fila:
        _,custo_atual, node = heapq.heappop(fila)
        contador += 1
        # print(f"DEBUG -- Custo atual: {custo_atual} | Nó atual: {node}")
        
        if node in visitados and visitados[node] <= custo_atual:
            continue
        
        visitados[node] = custo_atual
        
        if node == goal:
            print(f"O A* resolveu o tabuleiro em {contador} tentativas com um custo total de {custo_atual}.")
            return True
        
        for vizi in get_neighbors(node):
            custo_att = custo_atual + 1
            custo_estimado_att = custo_att + dist_manhatan(vizi, goal)
            heapq.heappush(fila, (custo_estimado_att, custo_att, vizi)) 
    return False


if __name__ == "__main__":
    # dist_manhatan(matriz_jogo_quinze, matriz_goal)

    unc(matriz_jogo_quinze, matriz_goal)
    
    astar(matriz_jogo_quinze, matriz_goal)