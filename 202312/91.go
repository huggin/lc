func numDecodings(s string) int {
	n := len(s)
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = -1
	}

	var f func(k int) int
	f = func(k int) int {
		if k == n {
			return 1
		}
		if dp[k] != -1 {
			return dp[k]
		}
		ans := 0
		if s[k] == '0' {
			dp[k] = 0
			return dp[k]
		}
		ans = f(k + 1)
		if k+1 < n && (s[k] == '1' || s[k] == '2' && s[k+1] <= '6') {
			ans += f(k + 2)
		}
		dp[k] = ans
		return ans
	}

	return f(0)
}
