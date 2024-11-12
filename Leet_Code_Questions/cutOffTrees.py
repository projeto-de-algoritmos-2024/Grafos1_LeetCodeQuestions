# https://leetcode.com/problems/cut-off-trees-for-golf-event/description/

from typing import List
from collections import deque

class Solution:

    # BFS que retornará a quantidade de passos necessários 
    
    def bfs(self, grafo: List[List[int]], start_x: int, start_y: int, target_x: int, target_y: int):
        m, n = len(grafo), len(grafo[0])

        if start_x == target_x and start_y == target_y:
            return 0
        visitado = [[False] * n for _ in range(m)]
        fila = deque([(start_x, start_y, 0)])
        visitado[start_x][start_y] = True

        while fila:
            x, y, passos = fila.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visitado[nx][ny] and grafo[nx][ny] > 0:
                    if nx == target_x and ny == target_y:
                        return passos + 1
                    fila.append((nx, ny, passos + 1))
                    visitado[nx][ny] = True
        return -1
        
    def cutOffTree(self, grafo: List[List[int]]) -> int:
        m, n = len(grafo), len(grafo[0])

        # Obter a lista de árvores a serem cortadas, ordenadas pela altura
        # No padrão (altura, i, j)

        arvores = sorted((grafo[i][j], i, j) for i in range(m) for j in range(n) if grafo[i][j] > 1)

        # Ponto inicial
        start_x, start_y = 0, 0
        total_passos = 0
 
        # Percorrer todas as árvores na ordem crescente de altura

        for _, x, y in arvores:
            passos = self.bfs(grafo, start_x, start_y, x, y)
            if passos == -1:
                return -1
            total_passos += passos
            start_x, start_y = x, y  # Atualizar o ponto de partida

        return total_passos

# Casos de teste

# solution = Solution()
# print(solution.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))  # Saída esperada: 6
# print(solution.cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))    # Saída esperada: -1
# print(solution.cutOffTree([[2,3,4],[0,0,5],[8,7,6]]))  # Saída esperada: 6