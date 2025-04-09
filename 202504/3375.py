class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        for a in nums:
            if a > k:
                s.add(a)
            elif a < k:
                return -1
        return len(s)
