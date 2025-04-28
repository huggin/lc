class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pres = [0]
        for a in nums:
            pres.append(pres[-1] + a)

        ans = 0
        j = 0
        n = len(nums)
        for i in range(n):
            while j < n and (pres[j + 1] - pres[i]) * (j - i + 1) < k:
                j += 1
            ans += j - i
        return ans
