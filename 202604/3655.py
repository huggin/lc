class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        b = isqrt(n)
        small = {}
        for l, r, k, v in queries:
            if k > b:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD
            else:
                rem = l % k
                i = (l - rem) // k
                j = (r - rem) // k
                key = (k, rem)
                if key not in small:
                    m = ((n - 1 - rem) // k + 1) if rem <= n - 1 else 0
                    small[key] = [1] * (m + 1)
                vec = small[key]
                vec[i] = (vec[i] * v) % MOD
                vec[j + 1] = vec[j + 1] * pow(v, -1, MOD) % MOD

        for (k, rem), v in small.items():
            curr = 1
            for i in range(len(v) - 1):
                curr = curr * v[i] % MOD
                j = rem + i * k
                nums[j] = nums[j] * curr % MOD

        return reduce(operator.xor, nums, 0)
