class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set()
        b = set()
        for n in nums1:
            if not n in nums2:
                a.add(n)

        for n in nums2:
            if not n in nums1:
                b.add(n)

        return [list(a), list(b)]
