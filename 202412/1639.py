class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        M = 10 ** 9 + 7
        freq = [[0 for _ in range(26)] for _ in range(m)]
        for w in words:
            for i in range(m):
                freq[i][ord(w[i])-ord('a')] += 1    

        @cache
        def f(k, j):
            if k == n:
                return 1
            if n - k > m - j:
                return 0
            ans = f(k, j+1) + f(k+1, j+1) * freq[j][ord(target[k])-ord('a')]
            return ans % M
        
        return f(0, 0)
