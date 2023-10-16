func getRow(rowIndex int) []int {
	var dp [2][34]int
	dp[0][0] = 1
	for i := 1; i <= rowIndex; i++ {
		dp[i%2][0] = 1
		dp[i%2][i] = 1
		for j := 1; j < i; j++ {
			dp[i%2][j] = dp[1-i%2][j-1] + dp[1-i%2][j]
		}
	}

	return dp[rowIndex%2][0 : rowIndex+1]
}
