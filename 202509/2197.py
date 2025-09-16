class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        s.append(nums[0])
        for i in range(1, len(nums)):
            curr = nums[i]
            while s:
                g = gcd(s[-1], curr)
                if g > 1:
                    t = s.pop()
                    curr = t * curr // g
                else:
                    break
            s.append(curr)
        return s
