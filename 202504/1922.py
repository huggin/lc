class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = n // 2
        even = n - odd
        M = 10 ** 9 + 7
        
        def exp(a, b):
            ans = 1
            while b > 0:
                if b & 1:
                    ans = ans * a % M
                b >>= 1
                a = a * a % M
            return ans
        
        return exp(5, even) * exp(4, odd) % M
