class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = [0] * 100
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            ans += cnt[a * 10 + b]
            cnt[a * 10 + b] += 1
        return ans
