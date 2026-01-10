# Não funciona com os goals
import random
from comuns import matriz_tuplo, dist_manhatan, GOALS, MAX_LIMIT

actions = {
    0: ("cima",    -1,  0),
    1: ("baixo",    1,  0),
    2: ("esquerda", 0, -1),
    3: ("direita",  0,  1),
}


# Ações Válidas no quadrado vazio
def actions_valida(estado):
    acao_valida = [0,0,0,0]
    
    # Posição do quadrado vazio
    p_vazia = estado.index(0)
    fila = p_vazia // 4
    coluna = p_vazia % 4
    
    # Encontrar opções válidas para a posição
    for action_id, (_,df,dc) in actions.items():
        new_fila = fila + df
        new_coluna = coluna + dc
        
        if 0 <= new_fila < 4 and 0 <= new_coluna < 4:
            acao_valida[action_id] = 1
    
    return acao_valida


# Reward em cada etapa
def reward(state,next_state, tipo_goal):
    goal = GOALS[tipo_goal]
    
    if next_state == goal:
        return 1000
    
    return dist_manhatan(state, tipo_goal) - dist_manhatan(next_state, tipo_goal)
  

# Modelo Q-Learn   
class PuzzleEnv:
    def __init__(self, estado, tipo_goal):
        self.state = estado
        self.tipo_goal = tipo_goal
        self.goal = GOALS[tipo_goal]
        
    def actions_valida(self):
        return actions_valida(self.state)
    
    def step(self, action_id):
        valida = self.actions_valida()
        if not valida[action_id]:
            return self.state, -10, False
        
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
        re = reward(self.state, novo_estado, self.tipo_goal)
        self.state = novo_estado
        
        fim = novo_estado == self.goal
        return novo_estado, re, fim
    
    def reset(self, estado):
        self.state = estado
        return self.state


# Treinar o mnodelo
def train_q_learning(env, episodes, max_steps,alpha=0.1, gamma=0.99, epsilon=1,epsilon_min=0.01,epsilon_decay=0.995,Q = None):
    if Q is None:
        print("DEBUG -- Modelo Q ainda não existe, a criar...")
        Q = {}
    
    estado_init = tuple(env.state)
    
    print("DEBUG -- Treino Começado...")
    for ep in range(episodes):
        state = env.reset(estado_init)
        step = 0
        
        while step < max_steps:
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
            Q[state][action] = Q[state][action] + alpha * (r + gamma * max(Q[prox_estado]) - Q[state][action])
            
            state = prox_estado
            step += 1
            
            if fim: break
        
        epsilon = max(epsilon_min, epsilon * epsilon_decay)
        
        if (ep + 1) % 500 == 0:
            print(f"DEBUG -- Episode {ep + 1} terminado")
    
    print("DEBUG -- Treino terminado...")
    return Q


# Testar o modelo
def test_policy(env, Q, max_steps):
    
    if max_steps == -1:
        max_steps = float("inf")
    
    state = env.reset(env.state)
    contador = 0
    
    print("Estado Inicial:")
    print([list(state[i:i+4]) for i in range(0,16,4)])
    
    while contador < max_steps:
        valid_actions = env.actions_valida()
        
        # Escolher a melhor ação
        q_vals = [Q.get(state, [0,0,0,0])[i] if valid_actions[i] else -float('inf') for i in range(4)]
        max_q = max(q_vals)
        best_actions = [i for i, q in enumerate(q_vals) if q == max_q]
        
        if max_q <= 0:
            action = random.choice([i for i,v in enumerate(valid_actions) if v])
        else:
            action = random.choice(best_actions)  

        next_state, r, fim = env.step(action)
        contador += 1
         
        if contador % 1000000 == 0:    
            print(f"DEBUG -- Step {contador}: Ação '{actions[action][0]}'")
            print([list(next_state[i:i+4]) for i in range(0,16,4)])
        
        state = next_state
 
        if fim:
            print(f"Tabuleiro resolvido em {contador} tentativas")
            return True
    
        if contador == MAX_LIMIT:
            print(f"O puzzle não foi resolvido em {contador} tentativas")
            return False
    
    print(f"O puzzle não foi resolvido em {max_steps} tentativas")
    return False
             
    
# Função Reinforcement Learning usada no main
def r_learning(initial_board,max_test_steps, tipo_goal,Q=None,episodes=10000, steps_treino = 3000):
    
    if max_test_steps == -1:
        max_steps = float("inf")
    
    initial_state = matriz_tuplo(initial_board)

    # Init Env
    env = PuzzleEnv(initial_state, tipo_goal)

    # Treino
    Q = train_q_learning(env,episodes = episodes, max_steps=steps_treino,Q=Q)

    env.reset(initial_state)

    # Testar a policy
    solu = test_policy(env, Q, max_steps)

    return solu, Q
        