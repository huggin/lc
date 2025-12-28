class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            if nums[i] == 0:
                left = sum(nums[0:i])
                right = sum(nums[i + 1 : n])
                if left == right:
                    ans += 2
                elif left + 1 == right or left == right + 1:
                    ans += 1
        return ans
