class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        def f(a, b):
            n = len(a)
            cnt = 0
            for i in range(n):
                if a[i] != b[i]:
                    cnt += 1
            return cnt <= 2

        for q in queries:
            for w in dictionary:
                if f(q, w):
                    ans.append(q)
                    break
        return ans
