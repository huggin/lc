class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        k -= 1
        sl = [2**i - 1 for i in range(1, n + 1)]
        inv = 0
        for l in reversed(sl):
            if l == 1:
                return "0" if inv == 0 else "1"
            if k == l // 2:
                return "1" if inv == 0 else "0"
            elif k > l // 2:
                k = l - 1 - k
                inv = 1 - inv
        return -1
