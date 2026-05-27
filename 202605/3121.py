class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        u = [0] * 26
        for c in word:
            if 'a' <= c <= 'z':
                i = ord(c) - ord('a')
                if u[i] != 1 and u[i] != -1:
                    u[i] = 2
                else:
                    u[i] = -1
            else:
                i = ord(c) - ord('A')
                if u[i] == 0:
                    u[i] = -1
                if u[i] != -1:
                    u[i] = 1
        return sum(1 if c == 1 else 0 for c in u)
