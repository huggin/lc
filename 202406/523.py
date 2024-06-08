class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1, len(nums)):
            if (nums[i] + nums[i - 1]) % k == 0:
                return True
        s = set()
        s.add(0)
        curr = 0
        for a in nums:
            if a % k == 0:
                continue

            curr = (curr + a) % k
            if curr in s:
                return True
            s.add(curr)
        return False
