func maxSumAfterPartitioning(arr []int, k int) int {
	n := len(arr)
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = -1
	}

	var f func(i int) int
	f = func(i int) int {
		if i == n {
			return 0
		}
		if dp[i] != -1 {
			return dp[i]
		}
		curr := 0
		ans := 0
		for j := i; j < min(i+k, n); j++ {
			curr = max(curr, arr[j])
			ans = max(curr*(j-i+1)+f(j+1), ans)
		}
		dp[i] = ans
		return ans
	}
	return f(0)
}
