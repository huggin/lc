class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (limit * 2 + 2)
        n = len(nums)
        for i in range(n // 2):
            mi, ma = nums[i], nums[n - 1 - i]
            if mi > ma:
                mi, ma = ma, mi
            diff[0] += 2
            diff[mi + 1] -= 1
            diff[mi + ma] -= 1
            diff[mi + ma + 1] += 1
            diff[ma + limit + 1] += 1

        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]

        return min(diff)
