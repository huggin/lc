class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx = [i for i, v in enumerate(nums) if v == key]
        ans = []
        for i, v in enumerate(nums):
            for j in idx:
                if abs(i - j) <= k:
                    ans.append(i)
                    break
        return ans
