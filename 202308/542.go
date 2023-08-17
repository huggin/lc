func updateMatrix(mat [][]int) [][]int {
	m := len(mat)
	n := len(mat[0])
	visited := make([][]byte, m)
	ans := make([][]int, m)
	var q []int
	for i := 0; i < m; i++ {
		visited[i] = make([]byte, n)
		ans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if mat[i][j] == 0 {
				visited[i][j] = 1
				q = append(q, i, j)
			}
		}
	}
	dx := [4]int{-1, 0, 0, 1}
	dy := [4]int{0, -1, 1, 0}
	dist := 0
	for len(q) > 0 {
		l := len(q)
		for i := 0; i < l/2; i++ {
			x := q[0]
			y := q[1]
			ans[x][y] = dist
			q = q[2:]
			for k := 0; k < 4; k++ {
				nx := x + dx[k]
				ny := y + dy[k]
				if nx >= 0 && nx < m && ny >= 0 && ny < n && visited[nx][ny] == 0 {
					q = append(q, nx, ny)
					visited[nx][ny] = 1
				}
			}
		}
		dist++
	}
	return ans
}
