class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        d = defaultdict(int)
        d[0] = 1
        curr = 0
        for i in range(n):
            curr += 1 if nums[i] % 2 else 0
            ans += d[curr - k]
            d[curr] += 1

        return ans
