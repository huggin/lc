class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        size = 0
        ans = 0
        for i in range(n, 0, -1):
            b = bin(i)[2:]
            ans = (i * (1 << size) + ans) % MOD
            size += len(b)
        return ans
