func isSubsequence(s string, t string) bool {
	m := len(s)
	n := len(t)
	i, j := 0, 0
	for ; i < m && j < n; j++ {
		if s[i] == t[j] {
			i++
		}
	}
	return i == m
}
