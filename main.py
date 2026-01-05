## Onde se vai escolher que algoritmo utilizar
from n_supervisonadas import dfs, bfs
from supervisionadas import unc, astar,gbfs
from ref_learning import r_learning

# matriz_goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,0]] Não é preciso

# Impossível
# matriz_jogo_quinze = [[2,5,6,8],[1,4,9,10],[12,14,15,3], [13,7,11,0]]
# matriz_jogo_quinze = [[14,13,15,7],[11,12,9,5],[6,0,2,1],[4,8,10,3]]

# Dificeis
#matriz_jogo_quinze = [[5, 0, 2, 11],[14, 1, 3, 6],[9, 8, 13, 7],[10, 15, 4, 12]]

# Médias
matriz_jogo_quinze = [[1,2,3,4],[5,6,0,8],[9,10,7,11],[13,14,15,12]]

# Fáceis
# matriz_jogo_quinze = [[1,2,3,4], [5,6,7,8], [9,14,10,12], [0,13,11,15]]
# matriz_jogo_quinze = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,0,15]]
def main():
    while True:
        print("\n" + "="*40)
        print("\tResolução Puzzle Jogo 15")
        print("="*40)
        print("Opções:")
        print("1 ➤ Procuras Não Supervisionadas")
        print("2 ➤ Procuras Supervisionadas")
        print("3 ➤ Reinforcement Learning")
        print("0 ➤ Encerrar")
        print("="*40)
        
        esc_init = input("Escolha uma opção: ").strip()
        
        if esc_init == "1":
            while True:
                print("\n--- Procura Não Supervisionadas ---")
                print("1 ➤ BFS")
                print("2 ➤ DFS")
                print("0 ➤ Regressar")
                esc_nsup = input("Escolha uma opção: ").strip()
                limite = input("Limite de Tentativas (-1 --> Limite Indeterminado): ").strip()
                
                if esc_nsup == "1":
                    bfs(matriz_jogo_quinze, limite)
                    break
                elif esc_nsup == "2":
                    dfs(matriz_jogo_quinze, limite)
                    break
                elif esc_nsup == "0":
                    break
                else:
                    print("Opção Inválida. Tente novamente.")
                    
        elif esc_init == "2":
            while True:
                print("\n--- Procura Supervisionadas ---")
                print("1 ➤ UNC")
                print("2 ➤ GBFS")
                print("3 ➤ A*")
                print("0 ➤ Regressar")
                esc_sup = input("Escolha uma opção: ").strip()
                
                if esc_sup in ["1","2","3"]:
                    limite = input("Limite de Tentativas (-1 --> Limite Indeterminado): ").strip()
                    if esc_sup == "1":
                        unc(matriz_jogo_quinze, limite)
                    elif esc_sup == "2":
                        gbfs(matriz_jogo_quinze, limite)
                    elif esc_sup == "3":
                        astar(matriz_jogo_quinze, limite)
                    break
                elif esc_sup == "0":
                    break
                else:
                    print("Opção Inválida. Tente novamente.")
                    
        elif esc_init == "3":
            print("\n--- Reinforcement Learning ---")
            limite = input("Limite de Tentativas (-1 --> Limite Indeterminado): ").strip()
            r_learning(matriz_jogo_quinze, limite)
            break
                 
        elif esc_init == "0":
            print("A encerrar o programa...")
            break  
        
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()
