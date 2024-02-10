func countSubstrings(s string) int {
	n := len(s)
	var dp [1000][1000]int
	ans := 0
	for i := 0; i < n; i++ {
		dp[i][i] = 1
		ans++
	}
	for k := 1; k < n; k++ {
		for i := 0; i+k < n; i++ {
			if s[i] == s[i+k] && (k == 1 || dp[i+1][i+k-1] == 1) {
				dp[i][i+k] = 1
				ans++
			}
		}
	}
	return ans
}
