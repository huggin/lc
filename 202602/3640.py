class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        j = -1
        turn = 0
        ans = -(10**15)
        nj = -1
        flag = False
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                j = -1
                nj = -1
                flag = False
            elif nums[i] > nums[i - 1]:
                flag = False
                if j != -1:
                    ans = max(ans, ps[i + 1] - ps[j])
                if i - 2 < 0 or nj == -1 or ps[i - 1] - ps[nj] < 0:
                    nj = i - 1
            else:
                if not flag:
                    j = nj
                    nj = -1
                    flag = True
        return ans
