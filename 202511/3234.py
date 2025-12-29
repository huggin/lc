class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [k for k, v in enumerate(s) if v == "0"]
        m = len(zeros)

        ans = 0
        for i in range(n):
            j = bisect_left(zeros, i)
            k = i
            zero = 0
            while j != m:
                idx = zeros[j]
                ones = idx - i - zero
                if ones >= zero * zero:
                    ans += min(ones - zero * zero + 1, idx - k)
                zero += 1
                k = idx
                j += 1
                if zero * zero > n - i:
                    break
            if j == m:
                ones = n - i - zero
                if ones >= zero * zero:
                    ans += min(ones - zero * zero + 1, n - k)

        return ans
