func removeDuplicateLetters(s string) string {
	cnt := make([]int, 26)

	for _, c := range s {
		cnt[c-'a']++
	}

	used := make([]int, 26)
	var ans []byte
	for _, c := range s {
		if used[c-'a'] == 1 {
			cnt[c-'a']--
			continue
		}
		for len(ans) > 0 && ans[len(ans)-1] > byte(c) && cnt[ans[len(ans)-1]-'a'] > 0 {
			used[ans[len(ans)-1]-'a'] = 0
			ans = ans[0 : len(ans)-1]
		}
		ans = append(ans, byte(c))
		cnt[c-'a']--
		used[c-'a'] = 1
	}

	return string(ans)
}
