class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        curr = []

        def f(k):
            if k == n:
                ans.append(curr[:])
                return

            f(k + 1)
            curr.append(nums[k])
            f(k + 1)
            curr.pop()

        f(0)
        return ans
