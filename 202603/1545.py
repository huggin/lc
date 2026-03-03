class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        for i in range(n):
            s = s + ['1'] + list('1' if c == '0' else '0' for c in reversed(s))
        
        return s[k-1]
