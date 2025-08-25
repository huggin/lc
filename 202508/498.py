class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m = len(mat)
        n = len(mat[0])
        ans = []
        flag = True
        for k in range(n+m-1):
            j = k - m + 1 if k >= m else 0
            i = k - j
            temp = []
            while j < n and i >= 0:
                temp.append(mat[i][j])
                j += 1
                i -= 1
            if flag:
                ans.extend(temp)
            else:
                ans.extend(reversed(temp))
            flag = not flag
        return ans
