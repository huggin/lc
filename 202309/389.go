func findTheDifference(s string, t string) byte {
	var cnt [26]int
	for i := 0; i < len(t); i++ {
		cnt[t[i]-'a']++
	}
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']--
	}
	for i := 0; i < 26; i++ {
		if cnt[i] == 1 {
			return byte(i + 'a')
		}
	}
	return 0
}
