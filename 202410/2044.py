class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        a = reduce(lambda x, y: x | y, nums)
        n = len(nums)
        self.ans = 0

        def dfs(k, curr):
            if n == k:
                if curr == a:
                    self.ans += 1
                return
            dfs(k + 1, curr)
            dfs(k + 1, curr | nums[k])

        dfs(0, 0)

        return self.ans
