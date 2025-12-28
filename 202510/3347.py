class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        a = []
        for c in nums:
            a.append(c)
            a.append(c - k)
            a.append(c + k)
        a = sorted(set(a))
        nums.sort()
        C = Counter(nums)
        n = len(nums)
        i, j, ans = 0, 0, 0
        for v in a:
            while i < n and nums[i] <= v + k:
                i += 1
            while j < n and nums[j] + k < v:
                j += 1

            if i - j > C[v] + numOperations:
                ans = max(ans, C[v] + numOperations)
            else:
                ans = max(ans, i - j)

        return ans
