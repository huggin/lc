a = []
prime = [1] * (10**6 + 1)
prime[1] = 0
for i in range(2, 10**6 + 1):
    if prime[i]:
        a.append(i)
        for j in range(i * i, 10**6 + 1, i):
            prime[j] = 0


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = len(a)
        v = 10**6
        ans = [-1, -1]
        for i in range(n - 1):
            if left <= a[i] and a[i + 1] <= right:
                if a[i + 1] - a[i] < v:
                    v = a[i + 1] - a[i]
                    ans[0] = a[i]
                    ans[1] = a[i + 1]
        return ans
