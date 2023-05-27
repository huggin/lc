class Solution:
    def solve(self, s1, s2, i, j):
        if i < 0 or j < 0:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if s1[i] == s2[j]:
            ans = 1 + self.solve(s1, s2, i - 1, j - 1)
        else:
            ans = max(self.solve(s1, s2, i - 1, j), self.solve(s1, s2, i, j - 1))

        self.dp[i][j] = ans
        return ans

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        self.dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.solve(nums1, nums2, n - 1, m - 1)
