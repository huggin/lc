class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        a = [0] * n
        for i in range(1, n):
            a[i] = a[i - 1] ^ derived[i - 1]

        if a[n - 1] ^ a[0] == derived[n - 1]:
            return True

        a = [1] * n
        for i in range(1, n):
            a[i] = a[i - 1] ^ derived[i - 1]

        if a[n - 1] ^ a[0] == derived[n - 1]:
            return True
        return False
