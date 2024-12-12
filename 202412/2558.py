class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []
        for gift in gifts:
            heapq.heappush(pq, -gift)

        while k > 0:
            heapq.heapreplace(pq, -int(math.sqrt(-pq[0])))
            k -= 1

        return -sum(pq)
