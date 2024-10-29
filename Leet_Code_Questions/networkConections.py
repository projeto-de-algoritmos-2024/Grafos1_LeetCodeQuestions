# https://leetcode.com/problems/critical-connections-in-a-network/

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        grafo = self.construir_grafo(n, connections)
        ids, menor_link = self.inicializar_rastreamento(n)
        tempo = [0]
        conexoes_criticas = []

        for i in range(n):
            if ids[i] == -1:
                self.dfs_pilha(i, grafo, ids, menor_link, conexoes_criticas, tempo)

        return conexoes_criticas

    def construir_grafo(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Constrói a lista de adjacências (grafo) a partir das conexões fornecidas.
        """
        grafo = [[] for _ in range(n)]
        for u, v in connections:
            grafo[u].append(v)
            grafo[v].append(u)
        return grafo

    def inicializar_rastreamento(self, n: int):
        """
        Inicializa os arrays `ids` e `menor_link` para rastrear o tempo de descoberta
        e o menor nó acessível em cada componente.
        """
        ids = [-1] * n  # ids dos nós (tempo de descoberta na DFS)
        menor_link = [-1] * n  # Menor id acessível para cada nó
        return ids, menor_link

    def dfs_pilha(self, inicio: int, grafo: List[List[int]], ids: List[int], menor_link: List[int], conexoes_criticas: List[List[int]], tempo: List[int]):
        """
        Realiza uma DFS iterativa utilizando uma pilha para identificar conexões críticas (pontes) no grafo.
        """
        pilha = [(inicio, -1)]  # Pilha para processar o nó e seu pai
        caminho = []  # Mantém o caminho atual da DFS

        while pilha:
            no_atual, pai = pilha[-1]

            if ids[no_atual] == -1:  # Se o nó ainda não foi visitado
                ids[no_atual] = tempo[0]
                menor_link[no_atual] = tempo[0]
                tempo[0] += 1
                caminho.append(no_atual)

            processado = True  # Inicialmente assumimos que todos os vizinhos foram processados

            for vizinho in grafo[no_atual]:
                if vizinho == pai:
                    continue  # Não revisitar o pai

                if ids[vizinho] == -1:
                    pilha.append((vizinho, no_atual))  # Adiciona o vizinho à pilha para processá-lo
                    processado = False  # Processar o vizinho antes de continuar
                    break
                else:
                    # Atualiza o menor_link com o menor valor de ids ou menor_link encontrado
                    menor_link[no_atual] = min(menor_link[no_atual], ids[vizinho])

            if processado:
                pilha.pop()

                if pai != -1 and menor_link[no_atual] > ids[pai]:
                    conexoes_criticas.append([pai, no_atual])

                if pai != -1:
                    menor_link[pai] = min(menor_link[pai], menor_link[no_atual])

# Casos de teste (remova os comentários para testar)

sol = Solution()
print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))  # Saída esperada: [[1, 3]]
print(sol.criticalConnections(2, [[0,1]]))  # Saída esperada: [[0, 1]]