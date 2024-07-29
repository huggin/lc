class Fenwick:
    def __init__(self, n):
        self.n = n + 1
        self.bit = [0] * self.n 
    
    def add(self, i, delta=1):
        i += 1
        while i < self.n:
            self.bit[i] += delta
            i += i&-i
    
    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.bit[i]
            i -= i&-i
        return ans

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        MAXN = 100001
        fen1 = Fenwick(MAXN)
        fen2 = Fenwick(MAXN)
        fen3 = Fenwick(MAXN)
        ans = 0
        for r in rating:
            ans += fen2.query(r-1)
            ans += fen3.query(MAXN-1) - fen3.query(r)
            fen2.add(r, fen1.query(r-1))
            fen3.add(r, fen1.query(MAXN-1) - fen1.query(r))
            fen1.add(r)
        return ans
