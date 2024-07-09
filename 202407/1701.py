class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tot = 0
        n = len(customers)
        curr = 0
        for a, t in customers:
            if curr <= a:
                tot += t
            else:
                tot += curr - a + t
            curr = max(curr, a) + t

        return tot / n
