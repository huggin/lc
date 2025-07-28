class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        a = reduce(operator.or_, nums)
        n = len(nums)
        ans = 0
        for i in range(1, 1 << n):
            t = 0
            for j in range(n):
                if i & (1 << j):
                    t |= nums[j]
            if t == a:
                ans += 1
        return ans
