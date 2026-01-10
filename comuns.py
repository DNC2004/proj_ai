# Não funciona com os goals
# Funções comuns a vários algoritmos
MAX_LIMIT = 100000000

GOALS = {
    "zf": (
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 0
    ),
    "zi": (
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11,
        12, 13, 14, 15
    ),
}



GOAL_POSITIONS = {

    name: {
        value: divmod(i, 4)
        for i, value in enumerate(goal)
    }
    
    for name, goal in GOALS.items()
}

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

def dist_manhatan(tabuleiro, goal_name): # Distância da posição atual do quadrado para a posição onde este é suposto estar
    dist = 0
    posicoes_pos = GOAL_POSITIONS[goal_name]
    
    
    for i, quadrado in enumerate(tabuleiro):
        if quadrado == 0:
            continue
        
        fila, coluna = divmod(i,4) # Posição do quadrado atual
        goal_fila, goal_coluna = posicoes_pos[quadrado] # Posição suposta do quadrado

        dist += abs(fila - goal_fila) + abs(coluna - goal_coluna) # Calcular a distância em si

        # DEBUG        
        # print(f"DEBUG -- O quadrado {quadrado} está na posição: x = {fila} | y = {coluna}") 
        # print(f"DEBUG -- O objetivo está na posição: x = {goal_fila} | y = {goal_coluna}") 
        # print(f"DEBUG -- Distância entre o quadrado {goal_fila} e {goal_coluna}: {dist}") 
    
    return dist