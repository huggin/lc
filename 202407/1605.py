class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        ans = [[0 for _ in range(m)] for _ in range(n)]

        def f(a):
            n = len(a)
            k = -1
            mi = int(1e9)
            for i in range(n):
                if a[i] < mi and a[i] > 0:
                    k = i
                    mi = a[i]
            return k

        while True:
            i = f(rowSum)
            j = f(colSum)
            if i == -1 or j == -1:
                break
            ans[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= ans[i][j]
            colSum[j] -= ans[i][j]
        return ans
