class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        tot = 0
        d = defaultdict(int)
        d[0] = 1
        ans = 0

        for a in nums:
            tot += a
            ans += d[tot - goal]
            d[tot] += 1

        return ans
