class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        ans = []
        for c in s:
            if c == ")" and cnt == 0:
                continue
            ans.append(c)
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1

        s2 = []
        for c in reversed(ans):
            if cnt > 0 and c == "(":
                cnt -= 1
                continue
            else:
                s2.append(c)

        return "".join(reversed(s2))
