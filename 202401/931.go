import "slices"

func minFallingPathSum(matrix [][]int) int {
	n := len(matrix)
	m := len(matrix[0])
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, m)
	}
	for i := 0; i < m; i++ {
		dp[0][i] = matrix[0][i]
	}
	for i := 1; i < n; i++ {
		for j := 0; j < m; j++ {
			dp[i][j] = dp[i-1][j]
			if j >= 1 {
				dp[i][j] = min(dp[i][j], dp[i-1][j-1])
			}
			if j+1 < m {
				dp[i][j] = min(dp[i][j], dp[i-1][j+1])
			}
			dp[i][j] += matrix[i][j]
		}
	}
	return slices.Min(dp[n-1])
}
