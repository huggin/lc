class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        arr.sort()
        n = len(arr)
        pq.append((arr[0] / arr[n - 1], 0, n - 1))
        used = [[0 for _ in range(n)] for _ in range(n)]
        used[0][n - 1] = 1
        while k > 1:
            curr, i, j = heapq.heappop(pq)
            if used[i + 1][j] == 0:
                heapq.heappush(pq, (arr[i + 1] / arr[j], i + 1, j))
                used[i + 1][j] = 1
            if used[i][j - 1] == 0:
                heapq.heappush(pq, (arr[i] / arr[j - 1], i, j - 1))
                used[i][j - 1] = 1
            k -= 1

        return [arr[pq[0][1]], arr[pq[0][2]]]
