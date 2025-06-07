class Solution:
    def clearStars(self, s: str) -> str:
        pos = [[] for _ in range(26)]
        n = len(s)
        used = [0] * n
        for k, c in enumerate(s):
            if c == '*':
                used[k] = 1
                for i in range(26):
                    if len(pos[i]) != 0:
                        used[pos[i][-1]] = 1
                        pos[i].pop()
                        break
            else:
                pos[ord(c) - ord('a')].append(k) 
        ans = []
        for i in range(n):
            if used[i] == 0:
                ans.append(s[i])
        return ''.join(ans)
