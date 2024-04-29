class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = 0
        for b in nums:
            a ^= b
        a ^= k
        ans = 0
        while a > 0:
            ans += 1
            a &= a - 1
        return ans
