@cache
def f(n, a, l):
    if n == 0:
        return 1
    ans = f(n - 1, a, 0)
    if a + 1 < 2:
        ans = (ans + f(n - 1, a + 1, 0)) % 1000000007
    if l + 1 < 3:
        ans = (ans + f(n - 1, a, l + 1)) % 1000000007
    return ans


class Solution:
    def checkRecord(self, n: int) -> int:
        return f(n, 0, 0)
