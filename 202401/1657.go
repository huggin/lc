import "sort"

func closeStrings(word1 string, word2 string) bool {
	var cnt, cnt2 [26]int
	for _, c := range word1 {
		cnt[c-'a']++
	}
	for _, c := range word2 {
		cnt2[c-'a']++
	}
	for i, v := range cnt {
		if v != 0 && cnt2[i] == 0 {
			return false
		}
	}
	sort.Ints(cnt[:])
	sort.Ints(cnt2[:])
	return cnt == cnt2
}
