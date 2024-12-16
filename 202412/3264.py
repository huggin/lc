class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            j = -1
            mi = float("inf")
            for i in range(len(nums)):
                if nums[i] < mi:
                    mi = nums[i]
                    j = i
            nums[j] *= multiplier

        return nums
