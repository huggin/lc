func ok(s string, f []int) bool {
	var t [26]int
	for i := 0; i < len(s); i++ {
		t[s[i]-'a']++
	}
	for i := 0; i < 26; i++ {
		if t[i] > f[i] {
			return false
		}
	}
	return true
}

func countCharacters(words []string, chars string) int {
	var freq [26]int
	for i := 0; i < len(chars); i++ {
		freq[chars[i]-'a']++
	}
	ans := 0
	for _, w := range words {
		if ok(w, freq[:]) {
			ans += len(w)
		}
	}
	return ans
}
