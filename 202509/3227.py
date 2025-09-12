class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        cnt = 0
        for c in s:
            if c in vowels:
                cnt += 1
        return cnt != 0
