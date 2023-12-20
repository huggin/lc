import "slices"

func buyChoco(prices []int, money int) int {
	slices.Sort(prices)
	ans := money - prices[0] - prices[1]
	if ans >= 0 {
		return ans
	}
	return money
}
