class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        ax = []
        for x, y, l in squares:
            events.append((y, x, x + l, 1))
            events.append((y + l, x, x + l, -1))
            ax.append(x)
            ax.append(x + l)

        events.sort()
        ax = sorted(set(ax))
        n = len(ax)
        length = [0] * (4 * n)
        cover = [0] * (4 * n)

        def update(v, l, r, tl, tr, val):
            if tr < l or r < tl:
                return
            if tl <= l and r <= tr:
                cover[v] += val
            else:
                mid = l + r >> 1
                update(v * 2, l, mid, tl, tr, val)
                update(v * 2 + 1, mid + 1, r, tl, tr, val)
            if cover[v] > 0:
                length[v] = ax[r + 1] - ax[l]
            elif l == r:
                length[v] = 0
            else:
                length[v] = length[v * 2] + length[v * 2 + 1]

        prev_y = events[0][0]
        segs = []
        for y, x1, x2, val in events:
            if prev_y < y:
                segs.append((prev_y, y, length[1]))

            l = bisect_left(ax, x1)
            r = bisect_left(ax, x2) - 1
            update(1, 0, n - 1, l, r, val)
            prev_y = y

        total = 0
        for y1, y2, x in segs:
            total += (y2 - y1) * x

        half = total / 2
        curr = 0
        ans = 0
        for y1, y2, x in segs:
            if curr + (y2 - y1) * x < half:
                curr += (y2 - y1) * x
            else:
                ans = (half - curr) / x + y1
                break
        return ans
