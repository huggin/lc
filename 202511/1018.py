class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        curr = 0
        for i in range(n):
            curr = curr * 2 + nums[i]
            if curr % 5 == 0:
                ans[i] = True
        return ans
