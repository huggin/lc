class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNext(u):
            ans = []
            dx = [10000, 1000, 100, 10]
            for d in dx:
                r = u % d
                b = u - r
                ans.append(b + (r + d // 10) % d)
                ans.append(b + (r + d // 10 * 9) % d)
            return ans

        target = int(target)
        s = set(map(int, deadends))
        if 0 in s:
            return -1
        if target == 0:
            return 0
        visited = [0] * 10000
        visited[0] = 1
        q = deque()
        q.append((0, 0))
        while len(q) > 0:
            u, l = q.popleft()
            for v in getNext(u):
                if v == target:
                    return l + 1
                if v not in s and visited[v] == 0:
                    visited[v] = 1
                    q.append((v, l + 1))
        return -1
