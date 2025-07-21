class Solution:
    def makeFancyString(self, s: str) -> str:
        a = []
        for c in s:
            if len(a) >= 2 and a[-1] == a[-2] and a[-1] == c:
                continue
            a.append(c)
        return "".join(a)
