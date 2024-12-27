class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            while len(st) > 0 and st[-1] > prices[i]:
                st.pop()
            if len(st) == 0:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - st[-1]
            st.append(prices[i])
        return ans
