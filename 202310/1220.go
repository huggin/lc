func countVowelPermutation(n int) int {
	dp := make([][5]int, n)
	mod := int(1e9 + 7)
	for i := 0; i < 5; i++ {
		dp[0][i] = 1
	}
	for i := 1; i < n; i++ {
		dp[i][0] = (dp[i-1][1] + dp[i-1][4] + dp[i-1][2]) % mod
		dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
		dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % mod
		dp[i][3] = dp[i-1][2]
		dp[i][4] = (dp[i-1][3] + dp[i-1][2]) % mod
	}
	ans := 0
	for i := 0; i < 5; i++ {
		ans = (ans + dp[n-1][i]) % mod
	}
	return ans
}
