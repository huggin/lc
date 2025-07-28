class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a = []
        for v in nums:
            if len(a) == 0 or a[-1] != v:
                a.append(v)

        n = len(a)
        ans = 0
        for i in range(1, n - 1):
            if (
                a[i - 1] < a[i]
                and a[i] > a[i + 1]
                or a[i - 1] > a[i]
                and a[i] < a[i + 1]
            ):
                ans += 1

        return ans
