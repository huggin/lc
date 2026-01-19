class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + mat[i][j]
        for k in range(min(n, m), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if (
                        ps[i + k][j + k] - ps[i][j + k] - ps[i + k][j] + ps[i][j]
                        <= threshold
                    ):
                        return k
        return 0
