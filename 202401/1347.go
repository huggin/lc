func minSteps(s string, t string) int {
	var cnt, cnt2 [26]int
	for _, c := range s {
		cnt[c-'a']++
	}
	for _, c := range t {
		cnt2[c-'a']++
	}
	ans := 0
	for i := 0; i < 26; i++ {
		ans += abs(cnt[i] - cnt2[i])
	}
	return ans / 2
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}
