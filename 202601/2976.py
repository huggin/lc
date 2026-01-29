class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        oo = int(1e9)
        a = ord("a")
        g = [[oo for _ in range(26)] for _ in range(26)]
        for i in range(26):
            g[i][i] = 0

        for i in range(len(original)):
            g[ord(original[i]) - a][ord(changed[i]) - a] = min(
                cost[i], g[ord(original[i]) - a][ord(changed[i]) - a]
            )

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        ans = 0
        for i in range(len(source)):
            if g[ord(source[i]) - a][ord(target[i]) - a] == oo:
                return -1
            ans += g[ord(source[i]) - a][ord(target[i]) - a]
        return ans
