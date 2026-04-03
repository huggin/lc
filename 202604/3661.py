class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        a = []
        n = len(robots)
        for i in range(n):
            a.append((robots[i], distance[i]))

        a.sort()
        walls.sort()

        def count(left, right):
            i = bisect_left(walls, left)
            j = bisect_right(walls, right)
            return j - i

        dp = [[0] * 2 for _ in range(n)]
        left = a[0][0] - a[0][1]
        dp[0][0] = count(left, a[0][0])
        right = a[0][0] + a[0][1]
        if n > 1 and a[1][0] <= right:
            right = a[1][0] - 1
        dp[0][1] = count(a[0][0], right)

        for i in range(1, n):
            left = max(a[i][0] - a[i][1], a[i - 1][0] + 1)
            dp[i][0] = dp[i - 1][0] + count(left, a[i][0])
            left = max(a[i][0] - a[i][1], right + 1)
            dp[i][0] = max(dp[i][0], dp[i - 1][1] + count(left, a[i][0]))
            right = a[i][0] + a[i][1]
            if i + 1 < n and a[i + 1][0] <= right:
                right = a[i + 1][0] - 1
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + count(a[i][0], right)

        return max(dp[-1])
