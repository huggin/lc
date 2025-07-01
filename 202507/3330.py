class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        n = len(word)
        for i in range(1, n):
            if word[i] == word[i-1]:
                ans += 1
        return ans

