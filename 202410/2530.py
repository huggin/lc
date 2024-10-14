class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-a for a in nums]
        heapq.heapify(nums)
        ans = 0
        while k > 0:
            a = -heapq.heappop(nums)
            ans += a
            a = (a + 2) // 3
            heapq.heappush(nums, -a)
            k -= 1
        return ans
