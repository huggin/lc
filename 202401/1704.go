func halvesAreAlike(s string) bool {
	n := len(s)
	cnt := 0
	for i := 0; i < n/2; i++ {
		if isVowels(s[i]) {
			cnt++
		}
	}
	for i := n / 2; i < n; i++ {
		if isVowels(s[i]) {
			cnt--
		}
	}

	return cnt == 0
}

func isVowels(c byte) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
		c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
}
