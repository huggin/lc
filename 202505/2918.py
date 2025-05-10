class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        c1 = sum(1 for a in nums1 if a == 0)
        c2 = sum(1 for a in nums2 if a == 0)
        if s1 > s2:
            s1, s2 = s2, s1
            c1, c2 = c2, c1

        if s1 == s2:
            if c1 == c2:
                return s1 + c1
            elif c1 > c2:
                if c2 == 0:
                    return -1
                else:
                    return s1 + c1
            else:
                if c1 == 0:
                    return -1
                else:
                    return s1 + c2
        else:
            if c1 == 0:
                return -1
            elif c2 == 0:
                if s1 + c1 > s2:
                    return -1
                else:
                    return s2
            else:
                return max(s2 + c2, s1 + c1)
