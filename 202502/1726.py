class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        d = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                ans += d[nums[i] * nums[j]]
                d[nums[i] * nums[j]] += 1

        return ans * 8
