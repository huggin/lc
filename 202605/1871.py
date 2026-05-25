class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        ps = [0] * (n + 1)
        for i in range(n):
            if i > 0:
                ps[i] += ps[i-1]
            if i == 0 or s[i] == '0' and ps[i] > 0:
                if i + minJump < n:
                    ps[i+minJump] += 1
                if i + maxJump + 1 < n:
                    ps[i+maxJump+1] -= 1
        return ps[n-1] > 0
                
