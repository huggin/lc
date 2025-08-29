class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        o1 = n // 2
        e1 = n - o1
        o2 = m // 2
        e2 = m - o2
        return o1 * e2 + o2 * e1
