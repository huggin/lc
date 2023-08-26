import "sort"

func findLongestChain(pairs [][]int) int {
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i][1] < pairs[j][1] {
			return true
		}
		return false
	})

	prev := -1001
	ans := 0
	for _, v := range pairs {
		if v[0] > prev {
			ans += 1
			prev = v[1]
		}
	}
	return ans
}
