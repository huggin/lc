class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [c for c in str(num)]
        for i in range(len(s)):
            k = i
            for j in range(i + 1, len(s)):
                if s[j] >= s[k]:
                    k = j
            if s[i] != s[k]:
                s[i], s[k] = s[k], s[i]
                break
        return int("".join(s))
