class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = index
        right = n - index - 1

        def valid(mid):
            d = mid
            if mid - 1 >= left:
                d += (2 * mid - left - 1) * left // 2
            else:
                d += mid * (mid - 1) // 2 + left - (mid - 1)

            if mid - 1 >= right:
                d += (2 * mid - right - 1) * right // 2
            else:
                d += mid * (mid - 1) // 2 + right - (mid - 1)

            return True if d <= maxSum else False

        ans = -1
        lo, hi = 1, maxSum
        while lo <= hi:
            mid = (lo + hi) // 2
            if valid(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
