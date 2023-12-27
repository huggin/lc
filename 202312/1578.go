func minCost(colors string, neededTime []int) int {
	ans := 0
	p := '#'
	curr := 0
	total := 0
	for k, c := range colors {
		total += neededTime[k]
		if p != c {
			ans += curr
			curr = neededTime[k]
		} else {
			curr = max(curr, neededTime[k])
		}
		p = c
	}
	ans += curr
	return total - ans
}
