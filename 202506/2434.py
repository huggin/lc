class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        n = len(s)
        mi = [None] * n
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        paper = []
        j = 0
        
        for i in range(26):
            c = chr(i + ord('a'))
            if c not in last:
                continue
            while len(paper) > 0 and paper[-1] <= c:
                ans.append(paper[-1])
                paper.pop()
            if last[c] >= j:
                for k in range(j, last[c] + 1):
                    if s[k] == c:
                        ans.append(c)
                    else:
                        paper.append(s[k])
                j = last[c] + 1

        return ''.join(ans)
        

