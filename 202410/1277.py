class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, n):
            matrix[0][i] += matrix[0][i-1]
        
        for i in range(1, m):
            matrix[i][0] += matrix[i-1][0]
            for j in range(1, n):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        
        ps = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = matrix[i][j]

        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(min(m, n)):
                    if i + k > m or j + k > n:
                        break
                    if ps[i+k][j+k] - ps[i-1][j+k] - ps[i+k][j-1] + ps[i-1][j-1] == (k + 1) ** 2:    
                        ans += 1
                
        return ans
