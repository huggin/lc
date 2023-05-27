class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        ma, mi = 0, 1000000
        for s in salary:
            total += s
            ma = max(ma, s)
            mi = min(mi, s)
        
        n = len(salary)
        return (total - ma - mi) / (n-2)
