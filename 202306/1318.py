class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:        
        ans = 0
        for i in range(31):
            if c >> i & 1 and (a >> i & 1) == 0 and (b >> i & 1) == 0:
                ans += 1
            elif (c >> i & 1) == 0:
                if a >> i & 1:
                    ans += 1
                if b >> i & 1:
                    ans += 1
        return ans
