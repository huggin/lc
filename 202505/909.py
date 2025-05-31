class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        vis = [-1] * (n * n + 1)
        vis[1] = 0
        q = deque()
        q.append(1)
        while q:
            curr = q.popleft()
            for i in range(1, 7):
                if curr + i > n * n:
                    continue
                nxt = curr + i
                if nxt == n * n:
                    return vis[curr] + 1
                x = n - 1 - (nxt - 1) // n
                y = (nxt - 1) % n if n % 2 == 1 and x % 2 == 0 or n % 2 == 0 and x % 2 == 1 else n-1-(nxt - 1) % n
                if board[x][y] != -1:
                    if board[x][y] == n * n:
                        return vis[curr] + 1
                    if vis[board[x][y]] == -1:
                        vis[board[x][y]] = vis[curr] + 1
                        q.append(board[x][y])
                elif vis[nxt] == -1:
                    vis[nxt] = vis[curr] + 1
                    q.append(nxt)

        return vis[n * n]


