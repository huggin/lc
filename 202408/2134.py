class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        ans = 0
        for i in range(ones):
            if nums[i] == 1:
                ans += 1

        curr = ans
        for i in range(ones, 2 * n):
            curr -= 1 if nums[(i - ones) % n] == 1 else 0
            curr += 1 if nums[i % n] == 1 else 0
            ans = max(ans, curr)

        return ones - ans
