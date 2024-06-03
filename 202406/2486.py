class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        m = len(s)
        j = 0
        k = n
        for i in range(n):
            while j < m and s[j] != t[i]:
                j += 1
            if j == m:
                k = i
                break
            else:
                j += 1

        return n - k
