class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(m):
            ans = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    ans[i][j] = m[j][n - 1 - i]

            return ans

        if mat == target:
            return True

        for _ in range(3):
            mat = rotate(mat)
            if mat == target:
                return True
        return False
