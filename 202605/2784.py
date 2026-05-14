class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = [0] * 201
        for a in nums:
            cnt[a] += 1
        for i in range(1, n):
            if cnt[i] == 0:
                return False
        return cnt[n - 1] == 2
