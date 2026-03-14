class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr = []
        self.ans = ""
        self.cnt = 0

        def dfs(i):
            if self.ans:
                return
            if i == n:
                self.cnt += 1
                if self.cnt == k:
                    self.ans = "".join(curr)
                return
            a = []
            for c in ["a", "b", "c"]:
                if i > 0 and curr[-1] == c:
                    continue
                a.append(c)

            for c in a:
                curr.append(c)
                dfs(i + 1)
                curr.pop()

        dfs(0)
        return self.ans
