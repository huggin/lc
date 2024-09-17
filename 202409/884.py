class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = defaultdict(int)
        for w in s1.split():
            s[w] += 1

        for w in s2.split():
            s[w] += 1

        ans = []
        for k, v in s.items():
            if v == 1:
                ans.append(k)
        return ans
