class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        a = []
        while n > 0:
            a.append(n % 3)
            n //= 3

        return not 2 in a
