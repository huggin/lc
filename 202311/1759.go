func countHomogenous(s string) int {
	mod := int64(1e9 + 7)
	var ans int64
	n := len(s)
	prev := byte(' ')
	var cnt int64
	for i := 0; i < n; i++ {
		if s[i] != prev {
			ans = (ans + (cnt+1)*cnt/2) % mod
			cnt = 1
		} else {
			cnt++
		}
		prev = s[i]
	}
	ans = (ans + (cnt+1)*cnt/2) % mod
	return int(ans % mod)
}
