class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        for i in range(len(s)):
            if s[i] == "1":
                if i != 0 and s[i] == s[i - 1]:
                    continue
                cnt += 1
        return cnt == 1
