class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)
        wordSet = set(wordDict)

        def solve(k, curr):
            if k == n:
                ans.append(" ".join(curr))
                return

            for i in range(k + 1, min(n + 1, k + 10)):
                if s[k:i] in wordSet:
                    curr.append(s[k:i])
                    solve(i, curr)
                    curr.pop()

        curr = []
        solve(0, curr)

        return ans
