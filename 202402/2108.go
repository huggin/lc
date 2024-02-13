func firstPalindrome(words []string) string {
	for _, w := range words {
		if ok(w) {
			return w
		}
	}
	return ""
}

func ok(s string) bool {
	n := len(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}
