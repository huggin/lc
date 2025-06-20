class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0

        def getMax(a):
            u = 0
            cnt = 0
            ans = 0
            for c in s:
                if c in a:
                    cnt += 1
                elif u < k:
                    u += 1
                    cnt += 1
                else:
                    cnt -= 1
                ans = max(ans, cnt)
            return ans

        ans = max(ans, getMax(["N", "E"]))
        ans = max(ans, getMax(["N", "W"]))
        ans = max(ans, getMax(["S", "E"]))
        ans = max(ans, getMax(["S", "W"]))
        return ans
