iclass Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        org = mat.copy()
        m = len(mat)
        n = len(mat[0])
        k %= n
        for i in range(m):
            if i & 1:
                mat[i] = org[i][n-k:] + org[i][0:n-k]
            else:
                mat[i] = org[i][k:] + org[i][0:k]
        return mat == org
