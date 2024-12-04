class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        j = 0
        for i in range(n):
            if j == m:
                return True
            if s1[i] == s2[j]:
                j += 1
            elif s1[i] == "z" and s2[j] == "a":
                j += 1
            elif 1 + ord(s1[i]) == ord(s2[j]):
                j += 1

        return j == m
