import random
from comuns import matriz_tuplo, dist_manhatan, GOAL

matriz_jogo_quinze = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]
#matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
#matriz_jogo_quinze = [[5, 0, 2, 11],[14, 1, 3, 6],[9, 8, 13, 7],[10, 15, 4, 12]]

#matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]
matriz_goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,0]]


actions = {
    0: ("cima",    -1,  0),
    1: ("baixo",    1,  0),
    2: ("esquerda", 0, -1),
    3: ("direita",  0,  1),
}

print(matriz_tuplo(matriz_goal))

def actions_valida(estado):
    # (1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,15)
    acao_valida = [0,0,0,0]
    
    p_vazia = estado.index(0)
    fila = p_vazia // 4
    coluna = p_vazia % 4
    
    for action_id, (_,df,dc) in actions.items():
        new_fila = fila + df
        new_coluna = coluna + dc
        
        if 0 <= new_fila < 4 and 0 <= new_coluna < 4:
            acao_valida[action_id] = 1
    
    return acao_valida

    
def reward(state, next_state, goal):
    if next_state == goal:
        return 100

    return (dist_manhatan(state,goal) - dist_manhatan(next_state, goal)) - 1
    
    
class PuzzleEnv:
    def __init__(self, estado):
        self.state = estado
        self.goal = GOAL
        
    def actions_valida(self):
        return actions_valida(self.state)
    
    def step(self, action_id):
        if not self.actions_valida()[action_id]:
            raise ValueError("ERRO -- Não existem ações válidas...")
        
        # Quadrado em vazio
        tile_vazio = self.state.index(0)
        fila_atual, coluna_atual = divmod(tile_vazio, 4)
        
        # Posição para mover 
        _, df, dc = actions[action_id]
        nova_fila = fila_atual + df
        nova_coluna = coluna_atual + dc
        nova_pos = nova_fila * 4 + nova_coluna
        
        # Realizar o movimento
        novo_estado = list(self.state)
        novo_estado[tile_vazio], novo_estado[nova_pos] = novo_estado[nova_pos], novo_estado[tile_vazio]

        novo_estado = tuple(novo_estado)
        
        # Calcular o reward
        re = reward(self.state, novo_estado, self.goal)
        self.state = novo_estado
        
        fim = novo_estado == self.goal
        return novo_estado, re, fim
    
    def reset(self, estado):
        self.state = estado
        return self.state
    
def train_q_learning(env, episodes=5000, alpha=0.1, gamma=0.99, epsilon=0.2, max_steps=200):
    Q = {} # Guarda o reward para cada ação
    
    for ep in range(episodes):
        state = env.reset(env.state)
        contador = 0
        
        while True:
            if state not in Q:
                Q[state] = [0, 0, 0, 0]
            
            valid_actions = env.actions_valida()
            
            # E greedy policy
            if random.random() < epsilon:
                # Explorar -- Escolhe uma das ações possíveis
                action = random.choice([i for i, v in enumerate(valid_actions) if v])
            else:
                # Escolhe a ação com o melhor max Q val
                q_vals = [Q[state][i] if valid_actions[i] else -float('inf') for i in range(4)]
                action = q_vals.index(max(q_vals))
            
            # Ação escolhida
            prox_estado, r, fim = env.step(action)
            
            if prox_estado not in Q:
                Q[prox_estado] = [0, 0, 0, 0]
            
            # Q-learning update
            Q[state][action] = Q[state][action] + alpha * (
                r + gamma * max(Q[prox_estado]) - Q[state][action]
            )
            
            state = prox_estado
            contador += 1
            if fim or contador >= max_steps:
                break
        
        if (ep + 1) % 500 == 0:
            print(f"Episode {ep + 1} finished")
    
    return Q


def test_policy(env, Q, max_steps=10000):
    state = env.reset(env.state)
    contador = 0
    print("Estado Inicial:")
    print([list(state[i:i+4]) for i in range(0,16,4)])
    
    while contador != max_steps:
        valid_actions = env.actions_valida()
        
        # Escolher a melhor ação
        q_vals = [Q.get(state, [0,0,0,0])[i] if valid_actions[i] else -float('inf') for i in range(4)]
        max_q = max(q_vals)
        
        best_actions = [i for i, q in enumerate(q_vals) if q == max_q]
        action = random.choice(best_actions)  

        next_state, r, fim = env.step(action)
        contador += 1
        print(f"Step {contador}: Ação '{actions[action][0]}'")
        print([list(next_state[i:i+4]) for i in range(0,16,4)])
        state = next_state
        
        if fim:
            print(f"Tabuleiro resolvido em {contador} tentativas")
            break
    
    print(f"O puzzle não foi resolvido em {contador} tentativas")
        
if __name__ == "__main__":
    initial_state = matriz_tuplo(matriz_jogo_quinze)
    env = PuzzleEnv(initial_state)
    Q = train_q_learning(env, episodes=2000)  # train for 2000 episodes
    env.reset(matriz_tuplo(matriz_jogo_quinze))
    test_policy(env, Q)
        
        