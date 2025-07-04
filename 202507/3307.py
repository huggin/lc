class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        n = len(operations)
        size = [0] * (n + 1)
        size[0] = 1
        for i in range(n):
            size[i + 1] = size[i] + size[i]

        add = 0
        for i in range(n - 1, -1, -1):
            o = operations[i]
            if o == 1 and k // size[i] == 1:
                add += 1
            k %= size[i]

        return chr(ord("a") + add % 26)
