func minTimeToVisitAllPoints(points [][]int) int {
	ans := 0
	n := len(points)
	for i := 1; i < n; i++ {
		ans += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
	}
	return ans
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}
