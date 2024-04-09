class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        n = len(tickets)
        for i in range(n):
            if i <= k:
                ans += min(tickets[k], tickets[i])
            else:
                ans += min(tickets[k] - 1, tickets[i])
        return ans
