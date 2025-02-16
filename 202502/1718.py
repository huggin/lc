class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (n * 2 - 1)
        m = len(ans)
        self.ans = None
        used = [0] * (n + 1)

        def dfs(k):
            if self.ans:
                return False
            if k == m:
                self.ans = ans[:]
                return True
            if ans[k] != 0:
                return dfs(k + 1)

            for i in range(n, 0, -1):
                if used[i] == 1:
                    continue
                if i == 1:
                    ans[k] = 1
                    used[1] = 1
                    if dfs(k + 1):
                        return True
                    used[1] = 0
                    ans[k] = 0
                elif ans[k] == 0 and i + k < m and ans[i + k] == 0:
                    ans[k] = i
                    ans[k + i] = i
                    used[i] = 1
                    if dfs(k + 1):
                        return True
                    used[i] = 0
                    ans[k] = 0
                    ans[k + i] = 0
            return False

        dfs(0)
        return self.ans
