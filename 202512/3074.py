class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        s = sum(apple)
        for i in range(len(capacity)):
            if s > capacity[i]:
                s -= capacity[i]
            else:
                return i + 1
        return len(capacity)
