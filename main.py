## Interface
import random
from n_informadas import dfs, bfs, unc
from informadas import astar,gbfs
from ref_learning import r_learning
from comuns import GOALS

# Impossível
# matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
matriz_jogo_quinze = [[14,13,15,7],[11,12,9,5],[6,0,2,1],[4,8,10,3]]

# Dificeis
#matriz_jogo_quinze = [[5, 0, 2, 11],[14, 1, 3, 6],[9, 8, 13, 7],[10, 15, 4, 12]]

# Médias
#matriz_jogo_quinze = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]

# Fáceis
# matriz_jogo_quinze = [[1,2,3,4], [5,6,7,8], [9,14,10,12], [0,13,11,15]]
# matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]

# Matrizes Professor
#matriz_jogo_quinze = [[2,8,12,15],[5,7,4,13],[1,3,11,10],[14,9,6,0]]


# Modelo vazio criado em cada run
Q = {}

# Gera matrizes no caso do utilizador não ter nenhuma previamente
def gen_matriz(dificuldade):
    
    # Objetivo
    matriz = [[1,2,3,4],[5,6,7,8],[9, 10, 11,12],[13,14,15,0]]

    # Número de movimentos por dificuldade
    movimentos = {
        1: random.randint(5, 10),
        2: random.randint(20, 40),
        3: random.randint(50, 60)
    }

    if dificuldade not in movimentos:
        raise ValueError("ERRO -- Dificuldade tem de ser: 1, 2, or 3")

    # Find empty tile
    def find_zero(m):
        for i in range(4):
            for j in range(4):
                if m[i][j] == 0:
                    return i, j

    # Movimentos Possíveis
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    x, y = find_zero(matriz)

    # Gerar a matriz
    for _ in range(movimentos[dificuldade]):
        valid_moves = []

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                valid_moves.append((nx, ny))

        nx, ny = random.choice(valid_moves)
        matriz[x][y], matriz[nx][ny] = matriz[nx][ny], matriz[x][y]
        x, y = nx, ny

    return matriz

def menu_tabuleiro():
    while True:
        print("\n╔═══════════════════════════════════════╗")
        print("║         ESCOLHER TABULEIRO            ║")
        print("╠═══════════════════════════════════════╣")
        print("║  [1] Gerar Tabuleiro                  ║")
        print("║  [2] Usar Tabuleiro Pré-definido      ║")
        print("║  [0] Regressar                        ║")
        print("╚═══════════════════════════════════════╝")


        op = input("Escolha: ").strip()

        if op == "1":               
            return menu_dificuldade()                   
        elif op == "2":
            return matriz_jogo_quinze
        elif op == "0":
            return None
        else:
            print("Opção inválida.")

# Dificuldades ao gerar matriz
def menu_dificuldade():
    while True:
        print("\n╔═══════════════════════════════════════╗")
        print("║            DIFICULDADE                ║")
        print("╠═══════════════════════════════════════╣")
        print("║  [1] Fácil                            ║")
        print("║  [2] Médio                            ║")
        print("║  [3] Difícil                          ║")
        print("║  [0] Regressar                        ║")
        print("╚═══════════════════════════════════════╝")

        op = input("Escolha: ").strip()

        if op in ["1", "2", "3"]:
            return gen_matriz(int(op))
        
        elif op == "0":
            return None
        
        else:
            print("Opção inválida.")

# Menu Principal Algoritmos
def menu_algoritmos(tabuleiro):
    global Q
    
    while True:
        print("\n╔═══════════════════════════════════════╗")
        print("║             ALGORITMOS                ║")
        print("╠═══════════════════════════════════════╣")
        print("║  [1] Procuras Não Informadas          ║")
        print("║  [2] Procuras Informadas              ║")
        print("║  [3] Reinforcement Learning           ║")
        print("║  [0] Regressar                        ║")
        print("╚═══════════════════════════════════════╝")


        op = input("Escolha: ").strip()

        if op == "1":
            menu_nao_informadas(tabuleiro)
        elif op == "2":
            menu_informadas(tabuleiro)
        elif op == "3":
            limite = int(input("Limite (-1 = ilimitado): "))
            solucao = False
            print("DEBUG -- Q existe, tamanho =", len(Q))
            
            for goal in ("zf", "zi"):
                print(f"DEBUG -- A testar o goal: {GOALS[goal]}")
                solved, Q = r_learning(tabuleiro,limite,goal, Q=Q)

                if solved:
                    print(f"DEBUG -- Resolvido com o goal: {goal}")
                    solucao = True
                    break 

            if not solucao:
                print("O || RL || não conseguiu encontrar uma solução para nenhuma das opções disponíveis.")

        elif op == "0":
            break
        else:
            print("Opção inválida.")



def menu_nao_informadas(tabuleiro):
    while True:
        print("\n╔═══════════════════════════════════════╗")
        print("║     PROCURAS NÃO INFORMADAS           ║")
        print("╠═══════════════════════════════════════╣")
        print("║  [1] BFS                              ║")
        print("║  [2] DFS                              ║")
        print("║  [3] UCS                              ║")
        print("║  [0] Regressar                        ║")
        print("╚═══════════════════════════════════════╝")


        op = input("Escolha: ").strip()

        if op == "1":
            limite = int(input("Limite (-1 = ilimitado): "))
            solucao = False
            
            for goal in ("zf", "zi"):
                print(f"DEBUG -- A testar o goal: {GOALS[goal]}")
            
                if bfs(tabuleiro, limite, goal):
                    print(f"DEBUG -- Resolvido com o goal: {goal}")
                    solucao = True
                    break

            if not solucao:
                print(f"O || BFS || não consiguiu encontrar uma solução para nenhuma das opções disponível.")
    
        elif op == "2":
            limite = int(input("Limite (-1 = ilimitado): "))
            solucao = False
            
            for goal in ("zf", "zi"):
                print(f"DEBUG -- A testar o goal: {GOALS[goal]}")
            
                if dfs(tabuleiro, limite, goal):
                    print(f"DEBUG -- Resolvido com o goal: {goal}")
                    solucao = True
                    break
                
        elif op == "3":
            limite = int(input("Limite (-1 = ilimitado): "))
            solucao = False
            
            for goal in ("zf", "zi"):
                print(f"DEBUG -- A testar o goal: {GOALS[goal]}")
            
                if unc(tabuleiro, limite, goal):
                    print(f"DEBUG -- Resolvido com o goal: {goal}")
                    solucao = True
                    break
            
            if not solucao:
                print(f"O || UCS || não consiguiu encontrar uma solução para nenhuma das opções disponível.")

        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_informadas(tabuleiro):
    while True:
        print("\n╔═══════════════════════════════════════╗")
        print("║      PROCURAS INFORMADAS              ║")
        print("╠═══════════════════════════════════════╣")
        print("║  [1] GBFS                             ║")
        print("║  [2] A*                               ║")
        print("║  [0] Regressar                        ║")
        print("╚═══════════════════════════════════════╝")

        esc = input("Escolha: ").strip()

        if esc == "1":
            limite = int(input("Limite (-1 = ilimitado): "))
            solucao = False
            
            for goal in ("zf", "zi"):
                print(f"DEBUG -- A testar o goal: {GOALS[goal]}")

                if gbfs(tabuleiro, limite, goal):
                    print(f"DEBUG -- Resolvido com o goal: {goal}")
                    solucao = True
                    break
            
            if not solucao:
                print(f"O || GBFS || não consiguiu encontrar uma solução para nenhuma das opções disponível.")
    
        elif esc == "2":
            limite = int(input("Limite (-1 = ilimitado): "))
            solucao = False
            
            for goal in ("zf", "zi"):
                print(f"DEBUG -- A testar o goal: {GOALS[goal]}")

                if astar(tabuleiro, limite, goal):
                    print(f"DEBUG -- Resolvido com o goal: {goal}")
                    solucao = True
                    break
            
            if not solucao:
                print(f"O || A* || não consiguiu encontrar uma solução para nenhuma das opções disponível.")
    
            if not solucao:
                print(f"O || A* || não consiguiu encontrar uma solução para nenhuma das opções disponível.")
            
        elif esc == "0":
            break
        else:
            print("Opção inválida.")


# Main
def main():
    tabuleiro = None

    while True:
        print("\n╔═══════════════════════════════════════╗")
        print("║      RESOLUÇÃO PUZZLE JOGO 15         ║")
        print("╠═══════════════════════════════════════╣")
        print("║  [1] Escolher Tabuleiro               ║")
        print("║  [2] Executar Algoritmos              ║")
        print("║  [0] Encerrar                         ║")
        print("╚═══════════════════════════════════════╝")


        op = input("Escolha: ").strip()

        if op == "1":
            tabuleiro = menu_tabuleiro()

            if tabuleiro:
                print("\nTabuleiro Atual:")
                for row in tabuleiro:
                    print(row)

        elif op == "2":
            if tabuleiro is None:
                print("Escolha primeiro um tabuleiro.")
            else:
                menu_algoritmos(tabuleiro)

        elif op == "0":
            print("A encerrar o programa...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    
    main()