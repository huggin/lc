func numberOfWays(corridor string) int {
	n := len(corridor)
	suf := make([]int, n)
	if corridor[n-1] == 'S' {
		suf[n-1] = 1
	}
	for i := n - 2; i >= 0; i-- {
		if corridor[i] == 'S' {
			suf[i] = suf[i+1] + 1
		} else {
			suf[i] = suf[i+1]
		}
	}
	if suf[0]%2 == 1 {
		return 0
	}
	const MOD = int(1e9 + 7)
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = -1
	}

	var f func(k int) int
	f = func(k int) int {
		if k == n || suf[k] == 2 {
			return 1
		}
		if dp[k] != -1 {
			return dp[k]
		}
		cnt := 0
		j := -1
		for i := k; i < n; i++ {
			if corridor[i] == 'S' {
				cnt++
			}
			if cnt == 2 {
				j = i
				break
			}
		}
		if j == -1 {
			dp[k] = 0
			return dp[k]
		}
		ans := f(j + 1)
		for i := j + 1; i < n; i++ {
			if corridor[i] == 'P' {
				ans = (ans + f(i+1)) % MOD
			} else {
				break
			}
		}
		dp[k] = ans
		return ans
	}

	return f(0)
}
