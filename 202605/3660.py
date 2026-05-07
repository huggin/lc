class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        ans = [pre[-1]] * n

        k = 0
        for i in range(0, n - 1):
            if pre[i] <= suf[i + 1]:
                for j in range(k, i + 1):
                    ans[j] = pre[i]
                k = i + 1

        return ans
