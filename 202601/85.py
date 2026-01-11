class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        def f(a):
            st = [(-1, -1)]
            ans = 0
            for i in range(m):
                while st[-1][1] > a[i]:
                    pi, ph = st.pop()
                    ans = max(ans, ph * (i - 1 - st[-1][0]))
                
                st.append((i, a[i]))

            while len(st) > 1:
                pi, ph = st.pop()
                ans = max(ans, (m - 1 - st[-1][0]) * ph)
            
            return ans
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = matrix[i-1][j] + 1

        ans = 0
        for i in range(n):
            ans = max(ans, f(matrix[i]))

        return ans
