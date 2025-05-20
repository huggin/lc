class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        cnt = [0] * (n + 1)
        for l, r in queries:
            cnt[l] += 1
            cnt[r + 1] -= 1

        for i in range(1, n + 1):
            cnt[i] += cnt[i - 1]

        for i in range(n):
            if cnt[i] < nums[i]:
                return False
        return True
