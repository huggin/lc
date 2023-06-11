class SnapshotArray:
    def __init__(self, length: int):
        self.store = {}
        self.id = 0
        self.len = length

    def set(self, index: int, val: int) -> None:
        if self.id not in self.store:
            self.store[self.id] = {}
        self.store[self.id][index] = val

    def snap(self) -> int:
        ans = self.id
        self.id += 1
        return ans

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if i in self.store and index in self.store[i]:
                return self.store[i][index]

        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
