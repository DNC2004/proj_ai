# Funções comuns a vários algoritmos
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
