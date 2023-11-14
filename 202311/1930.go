func countPalindromicSubsequence(s string) int {
	ans := 0
	n := len(s)
	presum := make([][26]int, n)
	presum[0][s[0]-'a']++
	for i := 1; i < n; i++ {
		presum[i] = presum[i-1]
		presum[i][s[i]-'a']++
	}
	first := make([]int, 26)
	for i := 0; i < 26; i++ {
		first[i] = -1
	}
	for i := 0; i < n; i++ {
		if first[s[i]-'a'] == -1 {
			first[s[i]-'a'] = i
		}
	}
	var cnt [26][26]int
	for i := 0; i < n; i++ {
		if first[s[i]-'a'] < i-1 {
			for j := 0; j < 26; j++ {
				if presum[i-1][j] > presum[first[s[i]-'a']][j] {
					cnt[s[i]-'a'][j] = 1
				}
			}
		}
	}
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			ans += cnt[i][j]
		}
	}
	return ans
}
