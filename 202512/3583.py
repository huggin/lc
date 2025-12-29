class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dp1 = {}
        dp2 = {}
        ans = 0
        MOD = 10**9 + 7
        for num in nums:
            if num % 2 == 0 and num // 2 in dp2:
                ans += dp2[num // 2]
            if num * 2 in dp1:
                dp2[num] = dp2.get(num, 0) + dp1[num * 2]
            dp1[num] = dp1.get(num, 0) + 1
        return ans % MOD
