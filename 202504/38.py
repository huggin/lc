class Solution:
    def countAndSay(self, n: int) -> str:
        def solve(s):
            c = s[0]
            cnt = 1
            ans = []
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    cnt += 1
                else:
                    ans.append(str(cnt))
                    ans.append(c)
                    c = s[i]
                    cnt = 1

            ans.append(str(cnt))
            ans.append(c)
            return ans

        s = "1"
        for _ in range(n - 1):
            s = solve(s)
        return "".join(s)
