class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        cnt = 0
        more, less = 0, 0
        mi1 = int(1e9)
        mi2 = int(1e9)
        for b in nums:
            a = b ^ k
            if a > b:
                cnt += 1
                more += a
                mi1 = min(mi1, a - b)
            else:
                less += b
                mi2 = min(mi2, b - a)

        if cnt % 2 == 0:
            return more + less

        return max(more + less - mi1, more + less - mi2)
