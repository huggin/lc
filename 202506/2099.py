class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i in range(k):
            heappush(pq, (nums[i], i))

        for i in range(k, len(nums)):
            if nums[i] > pq[0][0]:
                heapreplace(pq, (nums[i], i))

        return list(a[0] for a in sorted(pq, key=lambda x: x[1]))
