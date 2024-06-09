class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem = defaultdict(int)
        rem[0] = 1
        curr = 0
        ans = 0
        for c in nums:
            curr = (curr + c) % k
            ans += rem[curr]
            rem[curr] += 1
        return ans
