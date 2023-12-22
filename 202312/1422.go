func maxScore(s string) int {
	n := len(s)
	ans := 0
	cnt := make([]int, n)
	if s[0] == '0' {
		cnt[0] = 1
	}
	for i := 1; i < n; i++ {
		if s[i] == '0' {
			cnt[i] = cnt[i-1] + 1
		} else {
			cnt[i] = cnt[i-1]
		}
	}
	for i := 0; i < n-1; i++ {
		ans = max(ans, cnt[i]+n-(i+1)-(cnt[n-1]-cnt[i]))
	}
	return ans
}
