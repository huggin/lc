class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(lo, hi):
            cnt = 0
            while lo <= n:
                cnt += min(n + 1, hi) - lo
                lo *= 10
                hi *= 10
            return cnt

        k -= 1
        curr = 1
        while k > 0:
            cnt = count(curr, curr + 1)
            if k >= cnt:
                k -= cnt
                curr += 1
            else:
                curr *= 10
                k -= 1

        return curr
