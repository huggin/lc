func transpose(matrix [][]int) [][]int {
	n := len(matrix)
	m := len(matrix[0])
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			ans[i][j] = matrix[j][i]
		}
	}
	return ans
}
