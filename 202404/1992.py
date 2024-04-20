class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(land)
        m = len(land[0])
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    k = i + 1
                    while k < n and land[k][j] == 1:
                        k += 1
                    l = j + 1
                    while l < m and land[i][l] == 1:
                        l += 1
                    ans.append([i, j, k - 1, l - 1])
                    for ii in range(i, k):
                        for jj in range(j, l):
                            land[ii][jj] = 0
        return ans
