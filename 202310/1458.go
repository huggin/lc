func maxDotProduct(nums1 []int, nums2 []int) int {
	n := len(nums1)
	m := len(nums2)

	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, m)
		for j := 0; j < m; j++ {
			dp[i][j] = -1
		}
	}

	ans2 := int(-1e9)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			ans2 = max(ans2, nums1[i]*nums2[j])
		}
	}

	var f func(i, j int) int
	f = func(i, j int) int {
		if i == n || j == m {
			return 0
		}
		if dp[i][j] != -1 {
			return dp[i][j]
		}
		ans := nums1[i]*nums2[j] + f(i+1, j+1)
		ans = max(ans, f(i, j+1))
		ans = max(ans, f(i+1, j))
		dp[i][j] = ans
		return ans
	}
	ans := f(0, 0)
	if ans == 0 {
		return ans2
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
