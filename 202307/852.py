class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        lo, hi = 0, n - 1
        while lo < hi:
            mid1 = lo + (hi - lo) // 3
            mid2 = hi - (hi - lo) // 3
            if arr[mid1] == arr[mid2]:
                lo = mid1 + 1
                hi = mid1 - 1
            elif arr[mid1] < arr[mid2]:
                lo = mid1 + 1
            else:
                hi = mid2 - 1

        return lo
