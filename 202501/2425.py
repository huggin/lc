class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ans = 0
        if n & 1:
            for a in nums2:
                ans ^= a
        if m & 1:
            for a in nums1:
                ans ^= a
        return ans
