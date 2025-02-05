class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt = 0
        j = -1
        for i in range(n):
            if s1[i] != s2[i]:
                cnt += 1
                if j != -1:
                    if s1[j] != s2[i] or s1[i] != s2[j]:
                        return False
                j = i
        return cnt == 2 or cnt == 0
