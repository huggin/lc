func minDifficulty(job []int, d int) int {
	n := len(job)

	if n < d {
		return -1
	}
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, d+1)
		for j := 0; j <= d; j++ {
			dp[i][j] = -1
		}
	}
	const MX = int(1e9)

	var f func(k int, d int) int
	f = func(k int, d int) int {
		if n-k < d {
			return MX
		}
		if d == 0 {
			if k == n {
				return 0
			} else {
				return MX
			}
		}
		if dp[k][d] != -1 {
			return dp[k][d]
		}
		ans := MX
		curr := 0
		for i := k; i < n; i++ {
			curr = max(curr, job[i])
			ans = min(ans, curr+f(i+1, d-1))
		}
		dp[k][d] = ans
		return ans
	}

	ans := f(0, d)
	if ans >= MX {
		return -1
	}
	return ans
}
