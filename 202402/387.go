func firstUniqChar(s string) int {
	var freq [26]int
	for _, c := range s {
		freq[c-'a']++
	}
	for i, c := range s {
		if freq[c-'a'] == 1 {
			return i
		}
	}
	return -1
}
