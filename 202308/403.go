func canCross(stones []int) bool {
	dp := make(map[int]map[int]bool)
	if stones[1]-stones[0] != 1 {
		return false
	}
	n := len(stones)

	var f func(k, step int) bool
	f = func(k, step int) bool {
		if k == n-1 {
			return true
		}
		if _, ok := dp[k]; ok {
			if v2, ok2 := dp[k][step]; ok2 {
				return v2
			}
		} else {
			dp[k] = make(map[int]bool)
		}
		ans := false
		for i := k + 1; i < n && stones[i]-stones[k] <= step+1; i++ {
			if stones[i]-stones[k] == step+1 || stones[i]-stones[k] == step || stones[i]-stones[k] == step-1 {
				ans = ans || f(i, stones[i]-stones[k])
			}
		}
		dp[k][step] = ans
		return ans
	}

	return f(1, 1)
}
