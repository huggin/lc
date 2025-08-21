class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ans = 0
        
        def f(a):
            ans = 0
            st = []
            mi = [0] * m
            for i, v in enumerate(a):
                while len(st) > 0 and a[st[-1]] >= v:
                    st.pop()
                if len(st) == 0:
                    mi[i] = v * (i + 1)
                else:
                    mi[i] = v * (i - st[-1]) + mi[st[-1]]
                st.append(i)
            return sum(mi)
        
        for i in range(n):
            if i > 0:
                for j in range(m):
                    if mat[i][j] == 1:
                        mat[i][j] += mat[i-1][j]
            ans += f(mat[i])

        return ans
