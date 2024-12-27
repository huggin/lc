class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        curr = values[0]
        for i in range(1, len(values)):
            ans = max(ans, curr + values[i] - i)
            if curr < values[i] + i:
                curr = values[i] + i
        return ans
