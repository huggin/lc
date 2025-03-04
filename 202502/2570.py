class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        ans = []
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

        while i < m:
            ans.append(nums1[i])
            i += 1
        while j < n:
            ans.append(nums2[j])
            j += 1

        return ans
