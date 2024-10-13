class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        n = len(nums)
        ma = -100001
        for i in range(n):
            heapq.heappush(pq, (nums[i][0], i, 0))
            ma = max(ma, nums[i][0])

        a, b = 0, 200001
        while True:
            mi = pq[0][0]
            if ma - mi < b - a or ma - mi == b - a and mi < a:
                a, b = mi, ma
            i, j = pq[0][1], pq[0][2]
            if j < len(nums[i]) - 1:
                ma = max(ma, nums[i][j + 1])
                heapq.heapreplace(pq, (nums[i][j + 1], i, j + 1))
            else:
                break

        return [a, b]
