class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(j, curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            if j == n:
                return

            dfs(j + 1, curr)
            curr.append(j + 1)
            dfs(j + 1, curr)
            curr.pop()

        dfs(0, [])
        return ans
