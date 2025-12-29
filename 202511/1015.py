class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        if k == 1:
            return 1
        s = set()
        r = 1
        cnt = 1
        while r not in s:
            s.add(r)
            r = r * 10 + 1
            cnt += 1
            r %= k
            if r == 0:
                return cnt

        return -1
