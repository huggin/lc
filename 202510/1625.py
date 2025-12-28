class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        v = set()
        q = deque()
        v.add(s)
        q.append(s)
        while q:
            s = q.popleft()
            t = s[-b:] + s[0:-b]
            if t not in v:
                v.add(t)
                q.append(t)
            t = "".join(
                s[i] if i % 2 == 0 else str((int(s[i]) + a) % 10) for i in range(len(s))
            )
            if t not in v:
                v.add(t)
                q.append(t)
        return min(v)
