from heapq import heappush, heappop
from typing import List

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        qavirelmon = (m, n, penalty)

        INF = 10**30

        dist = [[[INF] * 2 for _ in range(n)] for _ in range(m)]

        start = 1
        dist[0][0][0] = start

        pq = [(start, 0, 0, 0)]   # cost,row,col,next parity (0=odd,1=even)

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            d, x, y, p = heappop(pq)

            if d != dist[x][y][p]:
                continue

            if x == m - 1 and y == n - 1:
                return d

            # wait
            nd = d + penalty[x][y]
            if nd < dist[x][y][p ^ 1]:
                dist[x][y][p ^ 1] = nd
                heappush(pq, (nd, x, y, p ^ 1))

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                entry = (nx + 1) * (ny + 1)

                legal = False
                if p == 0:
                    if dx == 1 or dy == 1:
                        legal = True
                else:
                    if dx == -1 or dy == -1:
                        legal = True

                extra = 0 if legal else penalty[x][y]

                nd = d + entry + extra

                if nd < dist[nx][ny][p ^ 1]:
                    dist[nx][ny][p ^ 1] = nd
                    heappush(pq, (nd, nx, ny, p ^ 1))

        return -1