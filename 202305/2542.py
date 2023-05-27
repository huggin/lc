import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = []
        n = len(nums1)
        for i in range(n):
            a.append((nums2[i], nums1[i]))

        a.sort(key=lambda x: (-x[1], x[0]))
        total = 0
        pq = []
        for i in range(k):
            total += a[i][1]
            heapq.heappush(pq, a[i])

        ans = total * pq[0][0]
        for i in range(k, n):
            if a[i][0] > pq[0][0]:
                total += a[i][1] - pq[0][1]
                heapq.heapreplace(pq, a[i])
            ans = max(ans, total * pq[0][0])

        return ans
