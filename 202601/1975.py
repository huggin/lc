class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        cnt = 0
        ma = inf
        for row in matrix:
            for item in row:
                if item <= 0:
                    cnt += 1
                    ans += -item
                    ma = min(ma, -item)
                else:
                    ans += item
                    ma = min(ma, item)
        if cnt % 2 == 0:
            return ans
        return ans - 2 * ma
