class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        cnt = [[0] * 26 for _ in range(2)]

        for i, c in enumerate(s1):
            cnt[i & 1][ord(c) - ord("a")] += 1

        for i, c in enumerate(s2):
            cnt[i & 1][ord(c) - ord("a")] -= 1
        for i in range(2):
            for j in range(26):
                if cnt[i][j] != 0:
                    return False
        return True
