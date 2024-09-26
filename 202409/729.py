from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.cal = SortedList()

    def book(self, start: int, end: int) -> bool:
        i = self.cal.bisect_left((start, end))
        if i >= 1 and self.cal[i - 1][1] > start:
            return False
        if i < len(self.cal) and self.cal[i][0] < end:
            return False
        self.cal.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
