class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            return int(str(x)[::-1])

        n = len(nums)
        ans = n
        d2i = {}
        for i in range(n):
            if nums[i] in d2i:
                ans = min(ans, i - d2i[nums[i]])
            d2i[reverse(nums[i])] = i
        return ans if ans != n else -1
