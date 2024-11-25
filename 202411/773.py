class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dst = (1, 2, 3, 4, 5, 0)
        q = deque()
        src = (
            board[0][0],
            board[0][1],
            board[0][2],
            board[1][0],
            board[1][1],
            board[1][2],
        )
        q.append(src)
        visited = {}
        visited[src] = 0

        while q:
            curr = q.popleft()
            if curr[0] == 0:
                n1 = (curr[1], curr[0], curr[2], curr[3], curr[4], curr[5])
                if n1 not in visited:
                    visited[n1] = visited[curr] + 1
                    q.append(n1)
                n2 = (curr[3], curr[1], curr[2], curr[0], curr[4], curr[5])
                if n2 not in visited:
                    visited[n2] = visited[curr] + 1
                    q.append(n2)
            elif curr[1] == 0:
                n1 = (curr[1], curr[0], curr[2], curr[3], curr[4], curr[5])
                if n1 not in visited:
                    visited[n1] = visited[curr] + 1
                    q.append(n1)
                n2 = (curr[0], curr[2], curr[1], curr[3], curr[4], curr[5])
                if n2 not in visited:
                    visited[n2] = visited[curr] + 1
                    q.append(n2)
                n3 = (curr[0], curr[4], curr[2], curr[3], curr[1], curr[5])
                if n3 not in visited:
                    visited[n3] = visited[curr] + 1
                    q.append(n3)
            elif curr[2] == 0:
                n1 = (curr[0], curr[2], curr[1], curr[3], curr[4], curr[5])
                if n1 not in visited:
                    visited[n1] = visited[curr] + 1
                    q.append(n1)
                n2 = (curr[0], curr[1], curr[5], curr[3], curr[4], curr[2])
                if n2 not in visited:
                    visited[n2] = visited[curr] + 1
                    q.append(n2)
            elif curr[3] == 0:
                n1 = (curr[0], curr[1], curr[2], curr[4], curr[3], curr[5])
                if n1 not in visited:
                    visited[n1] = visited[curr] + 1
                    q.append(n1)
                n2 = (curr[3], curr[1], curr[2], curr[0], curr[4], curr[5])
                if n2 not in visited:
                    visited[n2] = visited[curr] + 1
                    q.append(n2)
            elif curr[4] == 0:
                n1 = (curr[0], curr[1], curr[2], curr[4], curr[3], curr[5])
                if n1 not in visited:
                    visited[n1] = visited[curr] + 1
                    q.append(n1)
                n2 = (curr[0], curr[1], curr[2], curr[3], curr[5], curr[4])
                if n2 not in visited:
                    visited[n2] = visited[curr] + 1
                    q.append(n2)
                n3 = (curr[0], curr[4], curr[2], curr[3], curr[1], curr[5])
                if n3 not in visited:
                    visited[n3] = visited[curr] + 1
                    q.append(n3)
            elif curr[5] == 0:
                n1 = (curr[0], curr[1], curr[2], curr[3], curr[5], curr[4])
                if n1 not in visited:
                    visited[n1] = visited[curr] + 1
                    q.append(n1)
                n2 = (curr[0], curr[1], curr[5], curr[3], curr[4], curr[2])
                if n2 not in visited:
                    visited[n2] = visited[curr] + 1
                    q.append(n2)

        return visited[dst] if dst in visited else -1
