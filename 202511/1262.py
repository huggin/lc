class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        r = [[] for _ in range(3)]
        for num in nums:
            r[num % 3].append(num)

        ans = sum(nums)
        if ans % 3 == 0:
            return ans
        elif ans % 3 == 1:
            ans1, ans2 = 0, 0
            if len(r[1]) > 0:
                ans1 = ans - min(r[1])
            if len(r[2]) > 1:
                r[2].sort()
                ans2 = ans - r[2][0] - r[2][1]
            return max(ans1, ans2)
        else:
            ans1, ans2 = 0, 0
            if len(r[2]) > 0:
                ans1 = ans - min(r[2])
            if len(r[1]) > 1:
                r[1].sort()
                ans2 = ans - r[1][0] - r[1][1]
            return max(ans1, ans2)
        return 0
