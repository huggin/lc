class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def f(i):
            for j in range(i + 1, i + k):
                if nums[j] <= nums[j - 1]:
                    return False
            return True

        for i in range(n - k - k + 1):
            j = i + k
            if f(i) and f(j):
                return True
        return False
