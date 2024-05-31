class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = reduce(xor, nums)

        b = [0] * 32
        j = -1
        for i in range(32):
            for c in nums:
                if c & (1 << i):
                    b[i] ^= 1
                else:
                    b[i] ^= 0
            if b[i] == 1:
                j = i
                break

        ans = [0, 0]
        for c in nums:
            if c & (1 << j):
                ans[0] ^= c
            else:
                ans[1] ^= c
        return ans
