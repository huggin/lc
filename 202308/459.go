func repeatedSubstringPattern(s string) bool {
	n := len(s)
	for i := 1; i <= n/2; i++ {
		if n%i != 0 {
			continue
		}
		t := s[0:i]
		j := 0
		for ; j < n; j += i {
			if t != s[j:j+i] {
				break
			}
		}
		if j == n {
			return true
		}
	}
	return false
}
