import "slices"

func findContentChildren(g []int, s []int) int {
	slices.Sort(g)
	slices.Sort(s)
	ans := 0
	for i, j := 0, 0; i < len(g) && j < len(s); j++ {
		if g[i] <= s[j] {
			ans++
			i++
		}
	}
	return ans
}
