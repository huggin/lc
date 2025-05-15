class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        n = len(words)
        pg = -1
        for i in range(n):
            if groups[i] != pg:
                ans.append(words[i])
                pg = groups[i]
        return ans
