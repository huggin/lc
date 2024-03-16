class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        tot = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tot -= 1
            else:
                tot += 1
            if tot in d:
                ans = max(ans, i - d[tot])
            else:
                d[tot] = i

        return ans
