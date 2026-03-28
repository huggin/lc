class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def f(a):
            n = len(a)
            s = sum(a)
            curr = 0
            for i in range(n):
                curr += a[i]
                if curr + curr == s:
                    return True
                elif curr + curr < s:
                    if curr == s - curr - a[i + 1] or curr == s - curr - a[-1]:
                        return True
                else:
                    if curr - a[i] == s - curr or curr - a[0] == s - curr:
                        return True
            return False

        n = len(grid)
        if n == 1:
            return f(grid[0])
        m = len(grid[0])
        if m == 1:
            return f(list(grid[i][0] for i in range(n)))

        s = sum(c for row in grid for c in row)

        freq = defaultdict(int)
        freq2 = defaultdict(int)
        freq4 = defaultdict(int)
        for i in range(n):
            for j in range(m):
                freq[grid[i][j]] += 1

        freq3 = freq.copy()
        curr = 0
        for i in range(n):
            for j in range(m):
                freq[grid[i][j]] -= 1
                curr += grid[i][j]
                freq2[grid[i][j]] += 1
            if curr + curr == s:
                return True
            elif curr + curr < s:
                if i == n - 2:
                    if (
                        s - curr - grid[-1][0] == curr
                        or s - curr - grid[-1][-1] == curr
                    ):
                        return True
                elif freq[s - curr - curr] > 0:
                    return True
            else:
                if i == 0:
                    if curr - grid[0][0] == s - curr or curr - grid[0][-1] == s - curr:
                        return True
                elif freq2[curr - (s - curr)] > 0:
                    return True

        curr = 0
        for j in range(m):
            for i in range(n):
                freq3[grid[i][j]] -= 1
                curr += grid[i][j]
                freq4[grid[i][j]] += 1
            if curr + curr == s:
                return True
            elif curr + curr < s:
                if j == m - 2:
                    if (
                        s - curr - grid[0][-1] == curr
                        or s - curr - grid[-1][-1] == curr
                    ):
                        return True
                elif freq3[s - curr - curr] > 0:
                    return True
            else:
                if j == 0:
                    if (
                        curr - grid[0][-1] == s - curr
                        or curr - grid[-1][-1] == s - curr
                    ):
                        return True
                elif freq4[curr - (s - curr)] > 0:
                    return True

        return False
