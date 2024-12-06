class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sb = set(banned)
        a = list(i for i in range(1, n + 1) if i not in sb)
        n = len(a)
        if n == 0 or a[0] > maxSum:
            return 0
        for i in range(1, n):
            a[i] += a[i - 1]
            if a[i] > maxSum:
                return i
        return n
