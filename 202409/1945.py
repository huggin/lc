class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def f(n):
            a = 0
            while n > 0:
                a += n % 10
                n //= 10
            return a

        a = [ord(c) - ord("a") + 1 for c in s]
        n = int("".join(map(str, a)))
        for _ in range(k):
            n = f(n)
        return n
