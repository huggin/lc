class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        curr = defaultdict(int)

        def f(i):
            nonlocal ans
            if i == n:
                ans += 1
                return

            f(i + 1)
            if curr[nums[i] - k] == 0:
                curr[nums[i]] += 1
                f(i + 1)
                curr[nums[i]] -= 1

        f(0)
        return ans - 1
