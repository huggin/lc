class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        v = [0] * n
        ans = []
        for c in nums:
            if v[c] == 1:
                ans.append(c)
            v[c] = 1
        return ans
