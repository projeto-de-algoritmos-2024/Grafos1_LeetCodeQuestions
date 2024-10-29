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
            caminho = []  # Caminho atual DFS (para backtracking)

            while pilha:
                no_atual, pai = pilha.pop()

                if ids[no_atual] == -1:  # Se o nó ainda não foi visitado
                    ids[no_atual] = tempo[0]
                    menor_link[no_atual] = tempo[0]
                    tempo[0] += 1
                    stack_info.append((no_atual, pai))
                    caminho.append(no_atual)

                    for vizinho in grafo[no_atual]:
                        if vizinho == pai:
                            continue  # Não revisitar o nó pai

                        if ids[vizinho] == -1:
                            pilha.append((vizinho, no_atual))  # Adiciona o vizinho na pilha
                        else:
                            # Se o vizinho já foi visitado, faz a atualização de menor_link
                            menor_link[no_atual] = min(menor_link[no_atual], ids[vizinho])

                if stack_info and stack_info[-1][0] == no_atual:
                    stack_info.pop()  # Remove o estado após processar todos os vizinhos

                    # Verificação de ponte
                    if pai != -1 and menor_link[no_atual] > ids[pai]:
                        conexoes_criticas.append([pai, no_atual])

                    # Atualiza o menor_link do nó pai
                    if pai != -1:
                        menor_link[pai] = min(menor_link[pai], menor_link[no_atual])

        # Iniciar a DFS do nó 0 (supondo que o grafo seja conectado)
        for i in range(n):
            if ids[i] == -1:
                dfs_pilha(i)

        return conexoes_criticas
