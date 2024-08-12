class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for a in nums:
            if len(self.pq) < k:
                heapq.heappush(self.pq, a)
            elif a > self.pq[0]:
                heapq.heapreplace(self.pq, a)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
