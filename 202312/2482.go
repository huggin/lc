func onesMinusZeros(grid [][]int) [][]int {
	n := len(grid)
	m := len(grid[0])

	oneRow := make([]int, n)
	oneCol := make([]int, m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 1 {
				oneRow[i]++
				oneCol[j]++
			}
		}
	}
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		ans[i] = make([]int, m)
		for j := 0; j < m; j++ {
			ans[i][j] = 2*oneRow[i] + 2*oneCol[j] - n - m
		}
	}
	return ans
}
