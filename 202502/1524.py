class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        M = 10**9 + 7
        e, o = 0, 0
        ans = 0
        for a in arr:
            if a & 1:
                ans += e + 1
                e, o = o, e + 1
            else:
                ans += o
                e += 1
        return ans % M
