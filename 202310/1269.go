func numWays(steps int, arrLen int) int {
	dp := make([][]int, steps+1)
	for i := range dp {
		dp[i] = make([]int, steps+1)
		for j := 0; j <= steps; j++ {
			dp[i][j] = -1
		}
	}
	const M = int(1e9 + 7)
	var f func(int, int) int
	f = func(s, i int) int {
		if s == 0 {
			if i == 0 {
				return 1
			} else {
				return 0
			}
		}
		if i > s {
			return 0
		}
		if dp[s][i] != -1 {
			return dp[s][i]
		}
		ans := f(s-1, i)
		if i > 0 {
			ans = (ans + f(s-1, i-1)) % M
		}
		if i+1 < arrLen {
			ans = (ans + f(s-1, i+1)) % M
		}
		dp[s][i] = ans
		return ans
	}
	return f(steps, 0)
}
