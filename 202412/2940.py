class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(heights)
        m = len(queries)

        a = []
        for i in range(m):
            x, y = queries[i][0], queries[i][1]
            if queries[i][0] > queries[i][1]:
                x, y = y, x
            a.append((x, y, i))

        a.sort(key=lambda x: x[1])

        sl = SortedList()
        j = n - 1
        ans = [-1] * m

        for i in range(m - 1, -1, -1):
            while j > a[i][1]:
                while len(sl) > 0 and sl[0][0] < heights[j]:
                    sl.pop(0)
                sl.add((heights[j], j))
                j -= 1
            if a[i][0] == a[i][1] or heights[a[i][0]] < heights[a[i][1]]:
                ans[a[i][2]] = a[i][1]
                continue
            ma = max(heights[a[i][0]], heights[a[i][1]]) + 1

            k = sl.bisect_right((ma, 0))
            if k != len(sl):
                ans[a[i][2]] = sl[k][1]
        return ans
