class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            s = str(n)
            if max(s) >= str(7):
                continue
            cnt = defaultdict(int)
            for c in s:
                cnt[int(c)] += 1
            if (
                cnt[0] == 0
                and (cnt[1] == 0 or cnt[1] == 1)
                and (cnt[2] == 0 or cnt[2] == 2)
                and (cnt[3] == 0 or cnt[3] == 3)
                and (cnt[4] == 0 or cnt[4] == 4)
                and (cnt[5] == 0 or cnt[5] == 5)
                and (cnt[6] == 0 or cnt[6] == 6)
            ):
                return n

        return -1
