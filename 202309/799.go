func champagneTower(poured int, query_row int, query_glass int) float64 {
	var dp [105][105]float64
	dp[0][0] = float64(poured)
	for i := 0; i < 100; i++ {
		for j := 0; j <= i; j++ {
			if dp[i][j] > 1 {
				half := (dp[i][j] - 1) / 2
				dp[i+1][j] += half
				dp[i+1][j+1] += half
			}
		}
	}
	if dp[query_row][query_glass] >= 1 {
		return 1
	}
	return dp[query_row][query_glass]
}
