class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [0] * n
        ans[0] = 1
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            a, b, c = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            ans[i] = min(a, b, c)
            if ans[i] == ans[i2] * 2:
                i2 += 1
            if ans[i] == ans[i3] * 3:
                i3 += 1
            if ans[i] == ans[i5] * 5:
                i5 += 1

        return ans[n - 1]
