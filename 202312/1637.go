import "slices"

func maxWidthOfVerticalArea(points [][]int) int {
	n := len(points)
	x := make([]int, 0)
	for i := 0; i < n; i++ {
		x = append(x, points[i][0])
	}
	slices.Sort(x)
	ans := x[1] - x[0]
	for i := 2; i < n; i++ {
		ans = max(ans, x[i]-x[i-1])
	}
	return ans
}
