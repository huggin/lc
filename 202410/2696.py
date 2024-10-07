class Solution:
    def minLength(self, s: str) -> int:
        a = []
        for c in s:
            if c != 'B' and c != 'D':
                a.append(c)
            elif len(a) > 0 and (a[-1] == 'A' and c == 'B' or a[-1] == 'C' and c == 'D'):
                a.pop()
            else:
                a.append(c)
        
        return len(a)
