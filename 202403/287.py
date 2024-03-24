class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p = nums[0]
        q = nums[0]
        while True:
            p = nums[p]
            q = nums[nums[q]]
            if p == q:
                break

        p = nums[0]
        while p != q:
            q = nums[q]
            p = nums[p]
        return p
