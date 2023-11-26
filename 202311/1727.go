import "slices"

func largestSubmatrix(matrix [][]int) int {
	n := len(matrix)
	m := len(matrix[0])
	for i := 0; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[j][i] == 1 {
				matrix[j][i] += matrix[j-1][i]
			}
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		slices.Sort(matrix[i])
		for j := m - 1; j >= 0; j-- {
			if matrix[i][j] > 0 {
				ans = max(ans, matrix[i][j]*(m-j))
			}
		}
	}

	return ans
}
