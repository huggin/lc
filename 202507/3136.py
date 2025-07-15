class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False
        v, c, d = 0, 0, 0
        for w in word:
            if w in ["@", "#", "$"]:
                return False
            if w in "aeiouAEIOU":
                v += 1
            elif w in "1234567890":
                d += 1
            else:
                c += 1
        return v > 0 and c > 0
