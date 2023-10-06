func integerBreak(n int) int {
	if n == 2 {
		return 1
	}
	if n == 3 {
		return 2
	}
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = -1
	}

	var f func(k int) int
	f = func(k int) int {
		if k == 0 {
			return 1
		}
		if dp[k] != -1 {
			return dp[k]
		}
		ans := f(k - 1)
		if k >= 2 {
			ans = max(ans, 2*f(k-2))
		}
		if k >= 3 {
			ans = max(ans, 3*f(k-3))
		}

		dp[k] = ans
		return ans
	}
	return f(n)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
