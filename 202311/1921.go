import "slices"

func eliminateMaximum(dist []int, speed []int) int {
	n := len(dist)
	time := make([]float64, n)
	for i := 0; i < n; i++ {
		time[i] = float64(dist[i]) / float64(speed[i])
	}
	slices.Sort(time)

	ans := 0
	for i := 0; i < n; i++ {
		if time[i]-float64(ans) > 1e-9 {
			ans++
		} else {
			break
		}
	}
	return ans
}
