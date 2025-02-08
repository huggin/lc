class NumberContainers:

    def __init__(self):
        self.d1 = {}
        self.d2 = {}

    def change(self, index: int, number: int) -> None:
        if index in self.d1:
            if self.d1[index] == number:
                return
            pn = self.d1[index]
            self.d2[pn].remove(index)
        self.d1[index] = number
        if number not in self.d2:
            self.d2[number] = SortedList()
        self.d2[number].add(index)

    def find(self, number: int) -> int:
        if number in self.d2 and len(self.d2[number]) > 0:
            return self.d2[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
