class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for a in nums:
            cnt[a] += 1

        cnt[1] += cnt[0]
        cnt[2] += cnt[1]

        n = len(nums)
        for i in range(n):
            if i < cnt[0]:
                nums[i] = 0
            elif i < cnt[1]:
                nums[i] = 1
            else:
                nums[i] = 2
