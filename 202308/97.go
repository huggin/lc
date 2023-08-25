func isInterleave(s1 string, s2 string, s3 string) bool {
	n := len(s1)
	m := len(s2)
	t := len(s3)
	if n+m != t {
		return false
	}
	if t == 0 {
		return true
	}
	var dp [101][101]int
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			dp[i][j] = -1
		}
	}

	var f func(i, j int) int
	f = func(i, j int) int {
		if i == n {
			if s2[j:m] == s3[i+j:t] {
				return 1
			} else {
				return 0
			}
		}
		if j == m {
			if s1[i:n] == s3[i+j:t] {
				return 1
			} else {
				return 0
			}
		}
		if dp[i][j] != -1 {
			return dp[i][j]
		}
		var ans int
		if s1[i] == s3[i+j] {
			ans |= f(i+1, j)
		}
		if s2[j] == s3[i+j] {
			ans |= f(i, j+1)
		}
		dp[i][j] = ans
		return ans
	}
	return f(0, 0) == 1
}
