class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(m):
            j = matrix[i].index(min(matrix[i]))
            ma = matrix[i][j]
            flag = True
            for k in range(m):
                if matrix[k][j] > ma:
                    flag = False
                    break
            if flag:
                ans.append(matrix[i][j])
        return ans
