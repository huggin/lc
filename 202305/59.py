class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x, y = 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        dr = 0
        min_c, max_c = 0, n - 1
        min_r, max_r = 0, n - 1
        curr = 1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        while curr <= n * n:
            ans[x][y] = curr
            curr += 1
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
