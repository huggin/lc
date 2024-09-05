class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        tot = mean * (n + m)
        s = sum(rolls)
        if s + n > tot or s + 6 * n < tot:
            return []
        need = tot - s
        a = need // n
        b = need % n
        return [a + 1] * b + [a] * (n - b)
