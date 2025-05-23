class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = sum(nums)
        a = []
        for c in nums:
            a.append((c ^ k) - c)

        a.sort(reverse=True)
        n = len(a)
        for i in range(0, n, 2):
            if i + 1 < n and a[i] + a[i + 1] > 0:
                ans += a[i] + a[i + 1]

        return ans
