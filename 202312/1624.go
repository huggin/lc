func maxLengthBetweenEqualCharacters(s string) int {
	var mark [26]int
	n := len(s)
	for i := 0; i < 26; i++ {
		mark[i] = -1
	}
	ans := -1
	for i := 0; i < n; i++ {
		if mark[s[i]-'a'] != -1 {
			ans = max(ans, i-mark[s[i]-'a']-1)
		} else {
			mark[s[i]-'a'] = i
		}
	}
	return ans
}
