class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        n = len(nums)
        pq = []
        j = 0
        ans = 0
        cnt = [0] * (n + 1)

        for i in range(n):
            while j < len(queries) and i == queries[j][0]:
                heapq.heappush(pq, -queries[j][1])
                j += 1

            if i > 0:
                cnt[i] += cnt[i - 1]

            while nums[i] > cnt[i]:
                if len(pq) == 0:
                    return -1
                y = -heapq.heappop(pq)
                if y < i:
                    continue
                ans += 1
                cnt[i] += 1
                cnt[y + 1] -= 1

        return len(queries) - ans
