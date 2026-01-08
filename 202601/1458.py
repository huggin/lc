class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        if max(nums1) < 0 and max(nums2) > 0:
            return max(nums1) * min(nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        @cache
        def f(i, j):
            if i == n or j == m:
                return 0
            return max(
                f(i + 1, j),
                f(i, j + 1),
                f(i + 1, j + 1),
                nums1[i] * nums2[j] + f(i + 1, j + 1),
            )

        return f(0, 0)
