class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        ma = c.most_common(1)[0][1]
        return sum(v for _, v in c.items() if v == ma)
