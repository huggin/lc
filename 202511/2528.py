class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lo, hi = 0, sum(stations) + k
        n = len(stations)

        def ok(v, k):
            s = stations.copy()
            curr = sum(s[0 : r + 1])
            if curr + k < v:
                return False
            if curr < v:
                s[r] += v - curr
                k -= v - curr
                curr = v
            for i in range(1, n):
                left = i - r - 1
                if left >= 0:
                    curr -= s[left]
                right = i + r
                if right < n:
                    curr += s[right]
                if curr + k < v:
                    return False
                if curr < v:
                    right = min(right, n - 1)
                    s[right] += v - curr
                    k -= v - curr
                    curr = v
            return True

        ans = 0
        while lo <= hi:
            v = lo + hi >> 1
            if ok(v, k):
                ans = v
                lo = v + 1
            else:
                hi = v - 1
        return ans
