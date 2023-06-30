from typing import List


class Solution:
    def find(self, k):
        while self.parent[k] != k:
            # self.parent[k] = self.parent[self.parent[k]]
            k = self.parent[k]
        return k

    def union(self, p, q):
        pi = self.find(p)
        qi = self.find(q)
        if pi == qi:
            return
        if self.count[pi] >= self.count[qi]:
            self.parent[qi] = pi
            self.count[pi] += self.count[qi]
        else:
            self.parent[pi] = qi
            self.count[qi] += self.count[pi]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        self.parent = [c for c in range(n + 2)]
        self.count = [1 for _ in range(n + 2)]

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        graph = [[1 for _ in range(col)] for _ in range(row)]

        for i in range(n - 1, -1, -1):
            x = cells[i][0] - 1
            y = cells[i][1] - 1
            graph[x][y] = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if ny < 0 or ny >= col:
                    continue
                if nx < 0:
                    self.union(x * col + y, n)
                elif nx == row:
                    self.union(x * col + y, n + 1)
                elif graph[nx][ny] == 0:
                    self.union(x * col + y, nx * col + ny)

            if self.connected(n, n + 1):
                return i

        return -1
