class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob = set()
        for x, y in obstacles:
            ob.add((x, y))

        ans = 0
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        x, y, k = 0, 0, 0
        for c in commands:
            if c == -1:
                k = (k + 1) % 4
            elif c == -2:
                k = (k + 3) % 4
            else:
                for i in range(c):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (nx, ny) in ob:
                        break
                    x, y = nx, ny
            ans = max(ans, x * x + y * y)

        return ans
