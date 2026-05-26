class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l, u = [0] * 26, [0] * 26
        for c in word:
            if "a" <= c <= "z":
                l[ord(c) - ord("a")] = 1
            if "A" <= c <= "Z":
                u[ord(c) - ord("A")] = 1
        return sum(1 if l[i] > 0 and u[i] > 0 else 0 for i in range(26))
