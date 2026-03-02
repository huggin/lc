class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zero = [0] * n
        for i in range(n):
            cnt = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    cnt += 1
                else:
                    break
            zero[i] = cnt

        ans = 0
        for i in range(n):
            if zero[i] >= n - 1 - i:
                continue
            k = -1
            for j in range(i + 1, n):
                if zero[j] >= n - 1 - i:
                    k = j
                    break
            if k == -1:
                return -1
            ans += k - i
            for j in range(k, i, -1):
                zero[j] = zero[j - 1]
        return ans
