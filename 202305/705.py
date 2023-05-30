class MyHashSet:
    def __init__(self):
        self.hash = [[] for _ in range(9973)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        idx = key % 9973
        self.hash[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % 9973
        j = -1
        for i in range(len(self.hash[idx])):
            if self.hash[idx][i] == key:
                j = i
                break

        if j != -1:
            self.hash[idx][-1], self.hash[idx][j] = (
                self.hash[idx][j],
                self.hash[idx][-1],
            )
            self.hash[idx].pop()

    def contains(self, key: int) -> bool:
        idx = key % 9973
        for i in range(len(self.hash[idx])):
            if self.hash[idx][i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
