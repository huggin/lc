from sortedcontainers import SortedList


class AllOne:

    def __init__(self):
        self.kc = {}
        self.list = SortedList()
        self.cs = {}

    def inc(self, key: str) -> None:
        if key not in self.kc:
            self.kc[key] = 1
        else:
            self.kc[key] += 1
        cnt = self.kc[key]
        if cnt - 1 >= 1:
            self.cs[cnt - 1].remove(key)
            if len(self.cs[cnt - 1]) == 0:
                self.list.remove(cnt - 1)
        if cnt not in self.cs:
            self.cs[cnt] = set()
        self.cs[cnt].add(key)
        if cnt not in self.list:
            self.list.add(cnt)

    def dec(self, key: str) -> None:
        self.kc[key] -= 1
        cnt = self.kc[key]
        self.cs[cnt + 1].remove(key)
        if len(self.cs[cnt + 1]) == 0:
            self.list.remove(cnt + 1)
        if cnt > 0:
            self.cs[cnt].add(key)
            if cnt not in self.list:
                self.list.add(cnt)

    def getMaxKey(self) -> str:
        if len(self.list) == 0:
            return ""
        return list(self.cs[self.list[-1]])[0]

    def getMinKey(self) -> str:
        if len(self.list) == 0:
            return ""
        return list(self.cs[self.list[0]])[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
