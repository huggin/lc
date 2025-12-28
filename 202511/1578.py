class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        cc = " "
        total, mi = 0, 0
        for i, color in enumerate(colors):
            if color != cc:
                ans += total - mi
                cc = color
                total = neededTime[i]
                mi = total
            else:
                total += neededTime[i]
                mi = max(mi, neededTime[i])
        return ans + total - mi
