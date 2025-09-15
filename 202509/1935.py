class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        n = len(words)
        cnt = 0
        for word in words:
            for c in word:
                if c in brokenLetters:
                    cnt += 1
                    break
        return n - cnt
