import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        pq = []
        n = len(nums1)
        m = len(nums2)
        ma = max(n, m)

        s = set()
        heapq.heappush(pq, (nums1[i] + nums2[j], i, j))
        while k > 0 and len(pq) > 0:
            _, i, j = heapq.heappop(pq)
            ans.append((nums1[i], nums2[j]))
            k -= 1
            if i + 1 < n and (i + 1) * ma + j not in s:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                s.add((i + 1) * ma + j)
            if j + 1 < m and i * ma + j + 1 not in s:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                s.add(i * ma + j + 1)

        return ans
