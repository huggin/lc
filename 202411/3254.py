class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        j = 0
        for i in range(k):
            if nums[i] > 0 and nums[i] != nums[i - 1] + 1:
                j = i

        for i in range(k, n):
            if i - j == k:
                ans.append(nums[i - 1])
                j += 1
            else:
                ans.append(-1)

            if nums[i] != nums[i - 1] + 1:
                j = i

        if n - j == k:
            ans.append(nums[n - 1])
        else:
            ans.append(-1)
        return ans
