func minWindow(s string, t string) string {
	cnt := [128]int{}
	cnt2 := [128]int{}
	distinct := 0
	for i := 0; i < len(t); i++ {
		cnt[t[i]]++
		if cnt[t[i]] == 1 {
			distinct++
		}
	}
	j := 0
	ans := len(s)
	left, right := -1, -1
	for i := 0; i < len(s); i++ {
		if cnt[s[i]] != 0 {
			cnt2[s[i]] += 1
			if cnt2[s[i]] == cnt[s[i]] {
				distinct--
				if distinct == 0 {
					for distinct == 0 {
						if ans >= i-j+1 {
							ans = i - j + 1
							left = j
							right = i
						}
						if cnt[s[j]] > 0 {
							cnt2[s[j]]--
							if cnt2[s[j]] < cnt[s[j]] {
								distinct++
							}
						}
						j++
					}
				}
			}
		}
	}
	if left == -1 {
		return ""
	}
	return s[left : right+1]
}
