class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rmi = [None] * (n + 1)
        rma = [None] * (n + 1)
        cmi = [None] * (n + 1)
        cma = [None] * (n + 1)
        for x, y in buildings:
            if rmi[x] is None:
                rmi[x] = y
                rma[x] = y
            else:
                rmi[x] = min(rmi[x], y)
                rma[x] = max(rma[x], y)
            if cmi[y] is None:
                cmi[y] = x
                cma[y] = x
            else:
                cmi[y] = min(cmi[y], x)
                cma[y] = max(cma[y], x)

        ans = 0
        for x, y in buildings:
            if rmi[x] < y < rma[x] and cmi[y] < x < cma[y]:
                ans += 1
        return ans
