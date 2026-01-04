class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        C = Counter(nums)
        for a in C.keys():
            b = isqrt(a)
            if b * b == a:
                continue
            cnt = 0
            d = -1
            for i in range(2, b + 1):
                if a % i == 0:
                    d = i
                    cnt += 1
            if cnt == 1:
                ans += C[a] * (1 + a + d + a // d)
        return ans
