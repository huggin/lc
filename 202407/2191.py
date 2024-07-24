class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {}

        def calc(a):
            digits = []
            while a > 0:
                digits.append(a % 10)
                a //= 10
            if len(digits) == 0:
                digits.append(0)
            ans = 0
            for c in reversed(digits):
                ans = ans * 10 + mapping[c]
            return ans

        for a in nums:
            d[a] = calc(a)

        nums.sort(key=lambda x: d[x])
        return nums
