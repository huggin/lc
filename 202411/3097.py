class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [[0 for _ in range(32)] for _ in range(n)]
        for i in range(n):
            for j in range(32):
                if nums[i] & (1 << j):
                    cnt[i][j] = 1
        curr = [0] * 32
        ans = n + 1
        l = 0
        for i in range(n):
            v = 0
            for j in range(32):
                curr[j] += cnt[i][j]
                if curr[j] > 0:
                    v |= 1 << j
            while v >= k and l <= i:
                ans = min(ans, i - l + 1)
                v = 0
                for j in range(32):
                    curr[j] -= cnt[l][j]
                    if curr[j] > 0:
                        v |= 1 << j
                l += 1

        return ans if ans < n + 1 else -1
