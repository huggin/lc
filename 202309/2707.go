func minExtraChar(s string, dict []string) int {
	n := len(s)
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = -1
	}

	dic := make(map[string]int)
	for _, d := range dict {
		dic[d] = 1
	}

	var f func(k int) int
	f = func(k int) int {
		if k == n {
			return 0
		}
		if dp[k] != -1 {
			return dp[k]
		}
		ans := 1 + f(k+1)
		for i := k; i < n; i++ {
			if dic[s[k:i+1]] == 1 {
				ans = min(ans, f(i+1))
			}
		}
		dp[k] = ans
		return ans
	}
	return f(0)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
