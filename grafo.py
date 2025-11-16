grafo = {
    "A" : ["B", "C", "D"],
    "B" : ["A", "C"],
    "C" : ["A", "B", "E"],
    "D" : ["A"],
    "E" : ["C", "F", "G"],
    "F" : ["E", "Goal"],
    "G" : ["E", "I", "H", "Goal"],
    "H" : ["G"],
    "I" : ["G", "Goal"],
    "Goal" : ["G", "I", "F"]
}

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
    print("🔹 Ordem nós gerados:", gerados)
    print("🔹 Ordem nós visitados:", visitados)
    print("🔹 Ordem nós expandidos:", expandidos)
    
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
                    
    print("🔹 Ordem nós gerados:", gerados)
    print("🔹 Ordem nós visitados:", visitados)
    print("🔹 Ordem nós expandidos:", expandidos)
    
bfs(grafo, "A", "Goal")
dfs(grafo, "A", "Goal")
    