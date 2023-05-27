class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y = 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        dr = 0
        n = len(matrix)
        m = len(matrix[0])
        min_c, max_c = 0, m - 1
        min_r, max_r = 0, n - 1
        ans = []
        k = n * m
        while k > 0:
            k -= 1
            ans.append(matrix[x][y])
            if x + dx[dr] > max_r:
                dr = (dr + 1) % 4
                max_c -= 1
            elif x + dx[dr] < min_r:
                dr = (dr + 1) % 4
                min_c += 1
            elif y + dy[dr] > max_c:
                dr = (dr + 1) % 4
                min_r += 1
            elif y + dy[dr] < min_c:
                dr = (dr + 1) % 4
                max_r -= 1

            x += dx[dr]
            y += dy[dr]
        return ans
