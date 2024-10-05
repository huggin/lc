class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if m > n:
            return False
        cnt = [0] * 26

        for c in s1:
            cnt[ord(c) - ord("a")] += 1

        cnt2 = [0] * 26
        for i in range(m):
            cnt2[ord(s2[i]) - ord("a")] += 1

        if cnt == cnt2:
            return True
        for i in range(m, n):
            cnt2[ord(s2[i - m]) - ord("a")] -= 1
            cnt2[ord(s2[i]) - ord("a")] += 1
            if cnt == cnt2:
                return True

        return False
