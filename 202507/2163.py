class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        pq = []
        n = len(nums)
        m = n // 3
        mi = [0] * n
        tt = 0
        for i in range(m):
            tt += nums[n - 1 - i]
            heappush(pq, nums[n - 1 - i])

        mi[2 * m] = tt
        for i in range(m, 2 * m):
            if nums[n - 1 - i] > pq[0]:
                tt += nums[n - 1 - i] - pq[0]
                heapreplace(pq, nums[n - 1 - i])
            mi[n - i - 1] = tt

        pq = []
        tt = 0
        for i in range(m):
            tt += nums[i]
            heappush(pq, -nums[i])

        ans = tt - mi[m]
        for i in range(m, 2 * m):
            if nums[i] < -pq[0]:
                tt += nums[i] + pq[0]
                heapreplace(pq, -nums[i])
            ans = min(ans, tt - mi[i + 1])

        return ans
