func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	var cnt [26]int
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	for i := 0; i < len(t); i++ {
		if cnt[t[i]-'a'] == 0 {
			return false
		}
		cnt[t[i]-'a']--
	}
	return true
}
