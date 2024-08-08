class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        x = rStart
        y = cStart
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = 0
        cnt = [1]
        for i in range(1, max(rows, cols)+1):
            cnt.append((8 * i))
        
        dist = 0
        curr = 0
        while len(ans) < rows * cols:
            if 0 <= x < rows and 0 <= y < cols:
                ans.append([x, y])
            curr += 1
            if dist < len(cnt) and cnt[dist] == curr:
                dist += 1
                curr = 0
            nx = x + dir[k][0]
            ny = y + dir[k][1]
            if max(abs(nx - rStart), abs(ny - cStart)) > dist:
                k = (k+1) % 4
                nx = x + dir[k][0]
                ny = y + dir[k][1]
            x, y = nx, ny
        return ans
