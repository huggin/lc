func numSpecial(mat [][]int) int {
	n := len(mat)
	m := len(mat[0])
	row := make([]int, n)
	col := make([]int, m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] == 1 {
				row[i]++
				col[j]++
			}
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] == 1 && row[i] == 1 && col[j] == 1 {
				ans++
			}
		}
	}
	return ans
}
