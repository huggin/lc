class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ps = [0]
        for a in nums:
            ps.append(ps[-1] + (1 if a % modulo == k else 0))

        d = defaultdict(int)
        ans = 0
        for i in range(len(ps)):
            ans += d[(ps[i] + modulo - k) % modulo]
            d[ps[i] % modulo] += 1
        return ans
