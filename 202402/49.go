func groupAnagrams(strs []string) [][]string {
	var ans [][]string
	ana := make(map[[26]int][]string)

	for _, s := range strs {
		var cnt [26]int
		for _, c := range s {
			cnt[c-'a']++
		}
		ana[cnt] = append(ana[cnt], s)
	}
	for _, v := range ana {
		ans = append(ans, v)
	}
	return ans
}
