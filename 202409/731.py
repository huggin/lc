from sortedcontainers import SortedList


class MyCalendarTwo:

    def __init__(self):
        self.a = SortedList()
        self.b = SortedList()

    def book(self, start: int, end: int) -> bool:
        i = self.b.bisect_left((start, end))
        if i < len(self.b) and self.b[i][0] < end:
            return False
        if i > 0 and self.b[i - 1][1] > start:
            return False
        a = []
        for i in range(len(self.a)):
            if self.a[i][1] <= start:
                a.append((self.a[i][0], self.a[i][1]))
            elif self.a[i][0] >= end:
                a.append((self.a[i][0], self.a[i][1]))
            elif start <= self.a[i][0] <= end and start <= self.a[i][1] <= end:
                self.b.add((self.a[i][0], self.a[i][1]))
                a.append((start, self.a[i][0] + 1))
                start = self.a[i][1]
            elif (
                self.a[i][0] <= start <= self.a[i][1]
                and self.a[i][0] <= end <= self.a[i][1]
            ):
                a.append((self.a[i][0], start))
                a.append((end, self.a[i][1]))
                self.b.add((start, end))
            elif self.a[i][0] <= start < self.a[i][1]:
                self.b.add((start, self.a[i][1]))
                a.append((self.a[i][0], start + 1))
                a.append((self.a[i][1], end))
            else:
                self.b.add((self.a[i][0], end))
                a.append((start, self.a[i][0] + 1))
                a.append((end, self.a[i][1]))

        self.a = SortedList(a)
        self.a.add((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
