class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        s = set(allowed)
        for w in words:
            flag = True
            for c in w:
                if c not in s:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans
