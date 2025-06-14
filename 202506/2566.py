class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = list(int(c) for c in str(num))
        n = len(s)
        ma = s[:]
        mi = s[:]
        found = -1
        for i in range(n):
            if found != -1:
                if s[i] == found:
                    ma[i] = 9
            elif s[i] != 9:
                found = s[i]
                ma[i] = 9

        found = -1
        for i in range(n):
            if found != -1:
                if s[i] == found:
                    mi[i] = 0
            elif s[i] != 0:
                found = s[i]
                mi[i] = 0

        return int("".join(str(c) for c in ma)) - int("".join(str(c) for c in mi))
