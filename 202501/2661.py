class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        d = [None] * (m * n + 1)
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)

        row = [0] * m
        col = [0] * n

        for k in range(len(arr)):
            i, j = d[arr[k]]
            row[i] += 1
            col[j] += 1
            if row[i] == n or col[j] == m:
                return k
        return -1
