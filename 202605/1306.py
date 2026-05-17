class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        v = [0] * n

        def dfs(k):
            v[k] = 1
            if k - arr[k] >= 0 and v[k - arr[k]] == 0:
                dfs(k - arr[k])
            if k + arr[k] < n and v[k + arr[k]] == 0:
                dfs(k + arr[k])

        dfs(start)

        for i in range(n):
            if v[i] and arr[i] == 0:
                return True
        return False
