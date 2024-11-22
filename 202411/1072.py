class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 1
        for i in range(n):
            temp = 1
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if matrix[i][k] == matrix[j][k]:
                        cnt += 1
                if cnt == 0 or cnt == m:
                    temp += 1
            ans = max(ans, temp)
        return ans
