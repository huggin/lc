class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j = -1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                j = i - 1
                break
        if j == -1:
            return 0

        k = -1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                k = i + 1
                break

        ans = j + 1
        for i in range(k, n):
            idx = bisect.bisect(arr, arr[i], hi=j + 1)
            ans = max(ans, idx + n - i)
        return n - ans
