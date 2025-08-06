class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        tree = [0] * (4 * n)

        def build(v, tl, tr):
            if tl == tr:
                tree[v] = baskets[tl]
                return
            tm = tl + tr >> 1
            build(v * 2, tl, tm)
            build(v * 2 + 1, tm + 1, tr)
            tree[v] = max(tree[2 * v], tree[v * 2 + 1])

        def query(v, tl, tr, f):
            if tree[v] < f:
                return -1
            if tl == tr:
                return tl
            tm = tl + tr >> 1
            left = query(v * 2, tl, tm, f)
            if left != -1:
                return left
            return query(v * 2 + 1, tm + 1, tr, f)

        def update(v, tl, tr, pos):
            if tl == tr:
                tree[v] = 0
                return
            tm = tl + tr >> 1
            if pos <= tm:
                update(v * 2, tl, tm, pos)
            else:
                update(v * 2 + 1, tm + 1, tr, pos)
            tree[v] = max(tree[v * 2], tree[v * 2 + 1])

        build(1, 0, n - 1)
        ans = 0
        for f in fruits:
            j = query(1, 0, n - 1, f)
            if j == -1:
                ans += 1
            else:
                update(1, 0, n - 1, j)

        return ans
