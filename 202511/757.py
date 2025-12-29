class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        s = SortedList()
        for a, b in intervals:
            if not s:
                s.add(b - 1)
                s.add(b)
            elif a <= s[-1] <= b and a <= s[-2] <= b:
                continue
            elif a <= s[-1] <= b:
                if b not in s:
                    s.add(b)
                else:
                    s.add(b - 1)
            elif a <= s[-2] <= b and b not in s:
                a.add(b)
            elif b not in s and b - 1 not in s:
                s.add(b - 1)
                s.add(b)
        return len(s)
