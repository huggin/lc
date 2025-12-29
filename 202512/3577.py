class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        if min(complexity[1:]) <= complexity[0]:
            return 0
        ans = 1
        for i in range(n - 1, 0, -1):
            ans = (ans * i) % MOD
        return ans
