import heapq
from comuns import matriz_tuplo, get_neighbors, dist_manhatan, GOALS, MAX_LIMIT
# Limite = -1 --> Não queremos limite

# Greedy Best First Search (Não contabiliza o custo só a distância)
def gbfs(matriz_tabuleiro, limite, tipo_goal):
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = GOALS[tipo_goal]
    
    fila = []
    heapq.heappush(fila, (dist_manhatan(tabuleiro, tipo_goal), tabuleiro))
    
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
            return False
        
        elif contador == MAX_LIMIT:
            print(f"O || GBFS || não resolveu o tabuleiro em {contador} tentativas.")
            return False
        
        
        if node in visitados:
            continue
        
        visitados.add(node)
        
        if node == goal:
            print(f"O || GBFS || resolveu o tabuleiro em {contador} tentativas.")
            return True
        
        for vizi in get_neighbors(node):
            if vizi not in visitados:
                heapq.heappush(fila, (dist_manhatan(vizi,tipo_goal),vizi))
    
    return False

# A* (Custo com heurística)
def astar(matriz_tabuleiro,limite, tipo_goal):
    fila = []
    tabuleiro = matriz_tuplo(matriz_tabuleiro)
    goal = GOALS[tipo_goal]
    
    heapq.heappush(fila, (dist_manhatan(tabuleiro, tipo_goal),0,tabuleiro))
    
    visitados = {}
    contador = 0
    
    while fila :
        _,custo_atual, node = heapq.heappop(fila)
        contador += 1
        # print(f"DEBUG -- Custo atual: {custo_atual} | Nó atual: {node}")
        
        if contador % 10000 == 0:
            print(f"Tentativa: {contador}")
            
        if contador == limite:
            print(f"O || A* || não resolveu o tabuleiro em {contador} tentativas.")
            return False
        
        elif contador == MAX_LIMIT:
            print(f"O || A* || não resolveu o tabuleiro em {contador} tentativas.")
            return False
        
        if node in visitados and visitados[node] <= custo_atual:
            continue
        
        visitados[node] = custo_atual
        
        
        if node == goal:
            print(f"O || A* || resolveu o tabuleiro em {contador} tentativas com um custo total de {custo_atual}.")
            return True
        
        for vizi in get_neighbors(node):
            custo_att = custo_atual + 1
            custo_estimado_att = custo_att + dist_manhatan(vizi,tipo_goal)
            heapq.heappush(fila, (custo_estimado_att, custo_att, vizi)) 
            
    return False
