func getLengthOfOptimalCompression(s string, k int) int {
	n := len(s)

	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, k+1)
		for j := 0; j <= k; j++ {
			dp[i][j] = -1
		}
	}
	var f func(i, j int) int
	f = func(i, j int) int {
		if j >= n-i {
			return 0
		}
		if dp[i][j] != -1 {
			return dp[i][j]
		}
		ans := n - i
		if j > 0 {
			ans = f(i+1, j-1)
		}
		for k := i; k < n; k++ {
			cnt, del := 0, 0
			for l := i; l <= k; l++ {
				if s[l] == s[i] {
					cnt++
				} else {
					del++
				}
			}
			if del <= j {
				curr := 1
				if cnt >= 100 {
					curr += 3
				} else if cnt >= 10 {
					curr += 2
				} else if cnt >= 2 {
					curr += 1
				}
				ans = min(ans, curr+f(k+1, j-del))
			}
		}
		dp[i][j] = ans
		return ans
	}

	return f(0, k)
}
