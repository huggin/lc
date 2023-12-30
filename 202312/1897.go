func makeEqual(words []string) bool {
	var cnt [26]int
	for _, w := range words {
		for _, c := range w {
			cnt[c-'a']++
		}
	}
	n := len(words)
	for i := 0; i < 26; i++ {
		if cnt[i]%n != 0 {
			return false
		}
	}
	return true
}
