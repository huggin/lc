func change(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1

	for _, c := range coins {
		for j := 0; j <= amount; j++ {
			if j >= c {
				dp[j] += dp[j-c]
			}
		}
	}
	return dp[amount]
}
