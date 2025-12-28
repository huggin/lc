class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev = [0] * 26
        for w in words:
            curr = [0] * 26
            for c in w:
                curr[ord(c) - ord("a")] += 1
            if prev != curr:
                ans.append(w)
                prev = curr
        return ans
