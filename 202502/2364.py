class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            ans += i - d[nums[i] - i]
            d[nums[i] - i] += 1
        return ans
