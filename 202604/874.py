class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob = set()
        for x, y in obstacles:
            ob.add((x, y))
        x, y, d = 0, 0, 0
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:
                for i in range(1, c+1):
                    nx = x + dr[d][0]
                    ny = y + dr[d][1]
                    if (nx, ny) in ob:
                        break
                    x = nx
                    y = ny
            ans = max(ans, x * x + y * y)
        return ans
