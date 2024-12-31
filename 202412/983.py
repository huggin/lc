class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @cache
        def f(k):
            if k == n:
                return 0
            ans = costs[0] + f(k+1)
            j1, j2 = n, n
            for i in range(k, n):
                if days[i] - days[k] >= 7 and j1 == n:
                    j1 = i
                if days[i] - days[k] >= 30:
                    j2 = i
                    break
            
            return min(ans, costs[1] + f(j1), costs[2] + f(j2))
        
        return f(0)
