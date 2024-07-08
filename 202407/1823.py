class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        flag = [False] * n
        curr = -1
        removed = 0
        while removed < n - 1:
            for _ in range(k):
                while True:
                    curr = (curr + 1) % n
                    if not flag[curr]:
                        break
            flag[curr] = True
            removed += 1

        for i in range(n):
            if not flag[i]:
                return i + 1
        return -1
