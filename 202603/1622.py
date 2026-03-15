MOD = 10**9 + 7


class Fancy:
    def __init__(self):
        self.val = []
        self.am = [(0, 1, 0)]

    def append(self, val: int) -> None:
        self.val.append(val)

    def addAll(self, inc: int) -> None:
        if len(self.val) == 0:
            return
        self.am.append((len(self.val), self.am[-1][1], (self.am[-1][2] + inc) % MOD))

    def multAll(self, m: int) -> None:
        if len(self.val) == 0:
            return
        self.am.append(
            (len(self.val), (self.am[-1][1] * m) % MOD, (self.am[-1][2] * m) % MOD)
        )

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.val):
            return -1

        i = bisect.bisect(self.am, (idx + 1, -1, -1)) - 1
        m = (self.am[-1][1] * pow(self.am[i][1], -1, MOD)) % MOD
        a = (self.am[-1][2] - (self.am[i][2] * m) % MOD + MOD) % MOD
        return (self.val[idx] * m + a) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
