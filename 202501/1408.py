class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w in words:
            for w2 in words:
                if w == w2:
                    continue
                if w2.find(w) != -1:
                    ans.append(w)
                    break
        return ans
