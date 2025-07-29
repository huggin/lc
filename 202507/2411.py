class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        cnt = [0] * 32
        n = len(nums)
        ma = [0] * n
        ma[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            ma[i] = ma[i + 1] | nums[i]
        ans = [1] * n
        j = 0

        def get():
            curr = 0
            for k in range(32):
                if cnt[k]:
                    curr |= 1 << k
            return curr

        for i in range(n):
            while j < n and get() != ma[i]:
                for k in range(32):
                    if nums[j] & (1 << k):
                        cnt[k] += 1
                j += 1

            ans[i] = max(j - i, 1)
            for k in range(32):
                if nums[i] & (1 << k):
                    cnt[k] -= 1

        return ans
