
import "slices"

func maxCoins(piles []int) int {
	slices.Sort(piles)
	n := len(piles)
	ans := 0
	for i := 0; i < n/3; i++ {
		ans += piles[n-2-i*2]
	}
	return ans
}
