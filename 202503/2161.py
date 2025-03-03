class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        le, gr, eq = 0, 0, 0
        for a in nums:
            if a < pivot:
                le += 1
            elif a > pivot:
                gr += 1
            else:
                eq += 1

        i = 0
        j = le
        k = le + eq
        ans = [0] * len(nums)
        for a in nums:
            if a < pivot:
                ans[i] = a
                i += 1
            elif a > pivot:
                ans[k] = a
                k += 1
            else:
                ans[j] = a
                j += 1
        return ans
