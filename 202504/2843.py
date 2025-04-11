class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n % 2 == 0:
                a = s[0 : n // 2]
                b = s[n // 2 : n]
                sa = sum(ord(c) - ord("0") for c in a)
                sb = sum(ord(c) - ord("0") for c in b)
                if sa == sb:
                    ans += 1
        return ans
