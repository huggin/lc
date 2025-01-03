class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = ["a", "e", "i", "o", "u"]
        a = [0] * (len(words) + 1)
        for i in range(len(words)):
            a[i + 1] = a[i] + 1 if words[i][0] in v and words[i][-1] in v else a[i]

        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = a[queries[i][1] + 1] - a[queries[i][0]]
        return ans
