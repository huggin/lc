class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))
        ans = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == mi:
                ans.append([arr[i - 1], arr[i]])
        return ans
