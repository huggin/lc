class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        a = [0]
        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) % 2 == 1:
                a.append(1)
            else:
                a.append(0)
            a[i] += a[i - 1]

        ans = [False] * len(queries)
        for i, v in enumerate(queries):
            ans[i] = a[v[1]] - a[v[0]] == v[1] - v[0]
        return ans
