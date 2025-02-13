class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        while nums:
            a = heapq.heappop(nums)
            if a >= k:
                break
            b = heapq.heappop(nums)
            heapq.heappush(nums, a * 2 + b)
            ans += 1

        return ans
