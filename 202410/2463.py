class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)
        oo = int(1e13)

        @cache
        def f(i, j, k):
            if i == n:
                return 0
            if j == m:
                return oo
            ans = f(i, j + 1, factory[j + 1][1] if j + 1 < m else 0)
            if k > 0:
                ans = min(ans, abs(robot[i] - factory[j][0]) + f(i + 1, j, k - 1))
            return ans

        return f(0, 0, factory[0][1])
