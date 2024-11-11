# https://leetcode.com/problems/contain-virus/description/

from typing import List
from collections import deque

class Solution:
    def bfs(self, grafo: List[List[int]]):
        m, n = len(grafo), len(grafo[0])

        regioes = []
        visitado = set()
            
        # BFS que retorna as regiões infectadas
        # O padrão da estrutura são 3 posições: A primeira região[0] é a região em si que está sendo infectada, sendo ela um set de par ordenado, como por exemplo {(0,0), (0,1)}
        # A segunda posição são as fronteiras, que são as regiões que futuramente seriam infectadas, também no padrão de par ordenado
        # A terceira posição é a quantidade de muros necessários para cobrir essa região infectada por completo

        for i in range(m):
            for j in range(n):
                if grafo[i][j] == 1 and (i, j) not in visitado:
                    regiao, fronteira, muros_necessarios = set(), set(), 0
                    fila = deque([(i, j)])
                    visitado.add((i, j))
                        
                    while fila:
                        x, y = fila.popleft()
                        regiao.add((x, y))
                        
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n:
                                if grafo[nx][ny] == 0:
                                    fronteira.add((nx, ny))
                                    muros_necessarios += 1
                                elif grafo[nx][ny] == 1 and (nx, ny) not in visitado:
                                    visitado.add((nx, ny))
                                    fila.append((nx, ny))
                        
                    regioes.append((regiao, fronteira, muros_necessarios))
            
        return regioes

    def containVirus(self, grafo: List[List[int]]) -> int:
        
        total_muros = 0
        
        # Loop até que todas as regiões estejam contidas ou o vírus se espalhe por toda a grade
        while True:
            # Utilizando BFS para obter as regiões infectadas e suas respectivas fronteiras e muros necessários
            regioes = self.bfs(grafo)
            
            # Se não houver mais regiões, o processo termina
            if not regioes:
                break
            
            # Encontra a região em que a fronteira(x[1]) é maior, ou seja, a que pode infectar mais pares.
            regiao_mais_ameacadora = max(regioes, key=lambda x: len(x[1]))
            
            total_muros += regiao_mais_ameacadora[2]
            
            # Marca a região como controlada passando uma flag para o par no grafo original
            for x, y in regiao_mais_ameacadora[0]:
                grafo[x][y] = -1
            
            # Espalha o vírus para todas as outras regiões
            for regiao, fronteira, _ in regioes:
                if regiao != regiao_mais_ameacadora[0]:  # Evita a região que foi contida
                    for x, y in fronteira:
                        grafo[x][y] = 1
        
        return total_muros

# Casos de teste

# solution = Solution()
# print(solution.containVirus([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]))  # Saída esperada: 10
# print(solution.containVirus([[1,1,1],[1,0,1],[1,1,1]]))    # Saída esperada: 4
# print(solution.containVirus([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]))  # Saída esperada: 13