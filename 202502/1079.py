class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        n = len(tiles)
        used = [0] * n

        def dfs(k, curr):
            if k == n:
                s.add("".join(curr))
                return
            dfs(k + 1, curr)
            for i in range(n):
                if used[i] == 0:
                    used[i] = 1
                    curr.append(tiles[i])
                    dfs(k + 1, curr)
                    curr.pop()
                    used[i] = 0

        curr = []
        dfs(0, curr)
        return len(s) - 1
