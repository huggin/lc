 class Solution:
    def mul(self, a, b, m):
        c = [[0 for _ in range(26)] for _ in range(26)]
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % m
        return c

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        M = int(1e9+7)
        a = [[0 for _ in range(26)] for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i]+1):
                a[(i+j)%26][i] = 1
        
        b = [0] * 26
        for c in s:
            b[ord(c) - 97] += 1

        r = [[0 for _ in range(26)] for _ in range(26)]
        for i in range(26):
            r[i][i] = 1

        while t > 0:
            if t & 1:
                r = self.mul(a, r, M)
            a = self.mul(a, a, M)
            t >>= 1
        
        c = [0] * 26
        for i in range(26):
            for j in range(26):
                c[i] += r[i][j] * b[j]
                c[i] %= M

        return sum(c) % M
