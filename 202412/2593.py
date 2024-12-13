class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = []
        for k, v in enumerate(nums):
            heapq.heappush(pq, (v, k))

        used = set()
        ans = 0
        while pq:
            v, k = heapq.heappop(pq)
            if k in used:
                continue
            ans += v
            used.add(k)
            used.add(k - 1)
            used.add(k + 1)
        return ans
