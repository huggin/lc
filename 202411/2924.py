class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deg = [0] * n
        for _, v in edges:
            deg[v] += 1

        cnt = 0
        j = -1
        for i in range(n):
            if deg[i] == 0:
                cnt += 1
                j = i
        return -1 if cnt != 1 else j
