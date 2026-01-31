class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        cnt = [0] * 26
        for c in letters:
            cnt[ord(c) - ord('a')] = 1
        for i in range(ord(target) - ord('a') + 1, 26):
            if cnt[i] == 1:
                return chr(ord('a') + i)
        return letters[0]
