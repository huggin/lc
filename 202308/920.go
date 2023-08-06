var dp [101][101]int

func numMusicPlaylists(n int, goal int, k int) int {
	fact := make([]int64, n+1)
	fact[0] = 1
	MOD := int64(1e9 + 7)
	for i := 1; i <= n; i++ {
		fact[i] = (fact[i-1] * int64(i)) % MOD
	}

	for i := 0; i < 101; i++ {
		for j := 0; j < 101; j++ {
			dp[i][j] = -1
		}
	}

	var f func(a, m int) int
	f = func(a, m int) int {
		if a > m {
			return 0
		}
		if a == m {
			return int(fact[a])
		}
		if dp[a][m] != -1 {
			return dp[a][m]
		}
		var ans int64
		if a > 0 {
			ans = ans + int64(a)*int64(f(a-1, m-1))
		}
		if n-a > k {
			ans = ans + int64(n-a-k)*int64(f(a, m-1))
		}
		ans %= MOD
		dp[a][m] = int(ans)
		return dp[a][m]
	}

	return f(n, goal)
}
