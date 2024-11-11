primes = [1] * 1001
primes[0] = primes[1] = 0
for i in range(2, 1001):
    if primes[i] == 1:
        for j in range(i * i, 1001, i):
            primes[j] = 0
prime = [i for i in range(len(primes)) if primes[i] == 1]


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = -1
        for i in range(len(nums)):
            j = bisect.bisect_left(prime, nums[i]) - 1
            t = nums[i]
            while j >= 0:
                if nums[i] - prime[j] > prev:
                    t = nums[i] - prime[j]
                    break
                j -= 1

            if t <= prev:
                return False
            prev = t

        return True
