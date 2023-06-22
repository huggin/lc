class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def f(k, buy):
            if k == n:
                return 0

            ans = f(k + 1, buy)
            if buy == 0:
                ans = max(ans, -prices[k] - fee + f(k + 1, 1 - buy))
            else:
                ans = max(ans, prices[k] + f(k + 1, 1 - buy))

            return ans

        return f(0, 0)
