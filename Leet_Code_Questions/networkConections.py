from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Lista de adjacências para representar o grafo
        grafo = [[] for _ in range(n)]
        for u, v in connections:
            grafo[u].append(v)
            grafo[v].append(u)

        # Variáveis principais para rastreamento
        ids = [-1] * n  # ids dos nós (tempo de descoberta na DFS)
        menor_link = [-1] * n  # Menor id acessível para cada nó
        tempo = [0]  # Tempo de descoberta DFS
        conexoes_criticas = []  # Para armazenar as pontes (conexões críticas)

        # Função DFS iterativa usando pilha
        def dfs_pilha(inicio):
            pilha = [(inicio, -1)]  # Iniciar a pilha com o nó inicial e sem nó pai
            stack_info = []  # Para armazenar o estado da DFS (nó, pai)

            # Armazenar menor_link para o caminho
            caminho = []

            while pilha:
                no_atual, pai = pilha[-1]  # Pegar o topo da pilha sem removê-lo
                if ids[no_atual] == -1:  # Se o nó ainda não foi visitado
                    ids[no_atual] = tempo[0]
                    menor_link[no_atual] = tempo[0]
                    tempo[0] += 1
                    caminho.append(no_atual)  # Adiciona o nó ao caminho de DFS

                processado = True  # Inicialmente, assumimos que todos os vizinhos foram processados

                # Agora exploramos os vizinhos do nó atual
                for vizinho in grafo[no_atual]:
                    if vizinho == pai:
                        continue  # Não revisitar o nó pai
                    if ids[vizinho] == -1:
                        pilha.append((vizinho, no_atual))  # Adiciona o vizinho à pilha para ser processado
                        processado = False  # Interrompe para processar o vizinho primeiro
                        break  # Para processar o próximo nó
                    else:
                        # Atualiza o menor_link com o valor do vizinho visitado anteriormente
                        menor_link[no_atual] = min(menor_link[no_atual], ids[vizinho])

                if processado:
                    # Após processar todos os vizinhos, verificar se há uma ponte
                    pilha.pop()  # Remover o nó atual da pilha após o processamento completo

                    if pai != -1 and menor_link[no_atual] > ids[pai]:
                        conexoes_criticas.append([pai, no_atual])

                    # Atualizar o menor_link do pai com base no menor_link do nó atual
                    if pai != -1:
                        menor_link[pai] = min(menor_link[pai], menor_link[no_atual])

        # Iniciar a DFS para todos os nós não visitados
        for i in range(n):
            if ids[i] == -1:
                dfs_pilha(i)

        return conexoes_criticas
