class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        a = []
        while n > 0:
            a.append(n % 3)
            n //= 3

        return 2 not in a
