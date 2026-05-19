class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)
        for a in nums1:
            if a in s:
                return a
        return -1
