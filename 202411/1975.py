class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cnt = 0
        mi = 10**5
        total = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    total -= matrix[i][j]
                    cnt += 1
                    mi = min(mi, -matrix[i][j])
                else:
                    total += matrix[i][j]
                    mi = min(mi, matrix[i][j])

        return total if cnt % 2 == 0 else total - mi - mi
