import "slices"

func findWinners(matches [][]int) [][]int {
	loser := make(map[int]int)
	all := make(map[int]bool)
	for _, m := range matches {
		loser[m[1]]++
		all[m[0]] = true
		all[m[1]] = true
	}
	ans := make([][]int, 2)
	for k := range all {
		if v, ok := loser[k]; !ok {
			ans[0] = append(ans[0], k)
		} else if v == 1 {
			ans[1] = append(ans[1], k)
		}
	}
	slices.Sort(ans[0])
	slices.Sort(ans[1])
	return ans
}
