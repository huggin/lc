class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                s.append(curr)

        s.sort()
        ans = 0
        M = int(1e9 + 7)
        for i in range(left - 1, right):
            ans += s[i]
            if ans >= M:
                ans -= M

        return ans
