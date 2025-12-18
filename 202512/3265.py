class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        ps =[0] * (n + 1)
        pp = [0] * (n + 1)
        for i in range(n):
            ps[i+1] = ps[i] + prices[i] * strategy[i]
            pp[i+1] = pp[i] + prices[i]

        ans = ps[-1]
        for i in range(n-k+1):
            ans = max(ans, ps[i] + pp[i+k] - pp[i+k//2] + ps[n] - ps[i+k])
        return ans
