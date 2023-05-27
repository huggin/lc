import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for d in nums:
            if len(self.pq) < k:
                heapq.heappush(self.pq, d)
            elif d > self.pq[0]:
                heapq.heapreplace(self.pq, d)
        print(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
