class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def f(k):
            ans = 0
            j = 0
            cnt = [0] * (n + 1)
            for i in range(n):
                cnt[nums[i]] += 1
                if cnt[nums[i]] == 1:
                    k -= 1
                    while k == 0:
                        ans += n - i
                        cnt[nums[j]] -= 1
                        if cnt[nums[j]] == 0:
                            k += 1
                        j += 1

            return ans

        return f(k) - f(k + 1)
