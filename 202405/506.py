import bisect


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = sorted(score)
        n = len(a)
        ans = [0] * n
        for i in range(n):
            j = bisect.bisect_left(a, score[i])
            if j == n - 1:
                ans[i] = "Gold Medal"
            elif j == n - 2:
                ans[i] = "Silver Medal"
            elif j == n - 3:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(n - j)
        return ans
