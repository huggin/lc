class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        ans = 28 * weeks + weeks * (weeks - 1) // 2 * 7
        if days != 0:
            ans += (1 + weeks + weeks + days) * days // 2
        return ans
