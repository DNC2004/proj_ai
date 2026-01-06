import heapq
from comuns import matriz_tuplo, get_neighbors, dist_manhatan, GOALS, MAX_LIMIT
# Impossível
# matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
# matriz_jogo_quinze = [[14,13,15,7],[11,12,9,5],[6,0,2,1],[4,8,10,3]]

# Dificeis
matriz_jogo_quinze = [[5, 0, 2, 11],[14, 1, 3, 6],[9, 8, 13, 7],[10, 15, 4, 12]]

# Médias
# matriz_jogo_quinze = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]

# Fáceis
# matriz_jogo_quinze = [[1,2,3,4], [5,6,7,8], [9,14,10,12], [0,13,11,15]]
# matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]
# Limite = -1 --> Não queremos limite

# Greedy Best First Search (Não contabiliza o custo só a distância)
def gbfs(matriz_tabuleiro, limite):
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = GOALS
    
    fila = []
    heapq.heappush(fila, (dist_manhatan(tabuleiro), tabuleiro))
    
    visitados = set()
    contador = 0
    
    while fila:
        _, node = heapq.heappop(fila)
        contador += 1
        # print(f"DEBUG -- Nó atual: {node}")
        
        if contador % 10000 == 0:
            print(f"Tentativa: {contador}")
            
        if contador == limite:
            print(f"O || GBFS || não resolveu o tabuleiro em {contador} tentativas.")
            break
        
        elif contador == MAX_LIMIT:
            print(f"O || GBFS || não resolveu o tabuleiro em {contador} tentativas.")
            break
        
        
        if node in visitados:
            continue
        
        visitados.add(node)
        
        if node == goal:
            print(f"O || GBFS || resolveu o tabuleiro em {contador} tentativas.")
            return True
        
        for vizi in get_neighbors(node):
            if vizi not in visitados:
                heapq.heappush(fila, (dist_manhatan(vizi),vizi))
    
    return False

# Uniforme Cost Search (Custo sem heurística)
def unc(matriz_tabuleiro,limite):
    fila = []
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = GOALS
    
    heapq.heappush(fila, (0, tabuleiro))
    
    visitados = {}
    contador = 0
    
    while fila:
        custo, node = heapq.heappop(fila)
        contador += 1
        #print(f"DEBUG -- Custo atual: {custo} | Nó atual: {node}")
        
        if contador % 10000 == 0:
            print(f"Tentativa: {contador}")
            
        if contador == limite:
            print(f"O || UCS || não resolveu o tabuleiro em {contador} tentativas.")
            break
        
        elif contador == MAX_LIMIT:
            print(f"O || UCS || não resolveu o tabuleiro em {contador} tentativas.")
            break
        
        
        if node in visitados and visitados[node] <= custo:
            continue
        
        visitados[node] = custo
        
        if node == goal:
            print(f"O || UCS || resolveu o tabuleiro em {contador} tentativas com um custo total de {custo}.")
            return True
        
        for vizi in get_neighbors(node):
            heapq.heappush(fila, (custo + 1, vizi))
    
    return False

# A* (Custo com heurística)
def astar(matriz_tabuleiro,limite):
    fila = []
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = GOALS
    
    heapq.heappush(fila, (dist_manhatan(tabuleiro),0,tabuleiro))
    
    visitados = {}
    contador = 0
    
    custos_menores = {tabuleiro: 0}
    
    while fila :
        _,custo_atual, node = heapq.heappop(fila)
        contador += 1
        # print(f"DEBUG -- Custo atual: {custo_atual} | Nó atual: {node}")
        
        if contador % 10000 == 0:
            print(f"Tentativa: {contador}")
            
        if contador == limite:
            print(f"O || A* || não resolveu o tabuleiro em {contador} tentativas.")
            break
        
        elif contador == MAX_LIMIT:
            print(f"O || A* || não resolveu o tabuleiro em {contador} tentativas.")
            break
        
        if node in visitados and visitados[node] <= custo_atual:
            continue
        
        visitados[node] = custo_atual
        
        
        if node == goal:
            print(f"O || A* || resolveu o tabuleiro em {contador} tentativas com um custo total de {custo_atual}.")
            return True
        
        for vizi in get_neighbors(node):
            custo_att = custo_atual + 1
            custo_estimado_att = custo_att + dist_manhatan(vizi)
            heapq.heappush(fila, (custo_estimado_att, custo_att, vizi)) 
    return False


if __name__ == "__main__":
    # dist_manhatan(matriz_jogo_quinze,

    #gbfs(matriz_jogo_quinze,0)
    #unc(matriz_jogo_quinze,0)
    astar(matriz_jogo_quinze,-1)