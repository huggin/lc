func garbageCollection(garbage []string, travel []int) int {
	ans := 0
	n := len(garbage)
	dist := make([]int, n)
	for i := 0; i < n-1; i++ {
		dist[i+1] = dist[i] + travel[i]
	}
	m, p, g := 0, 0, 0
	for i := 0; i < n; i++ {
		ans += len(garbage[i])
		for _, a := range garbage[i] {
			if a == 'M' {
				m = i
			} else if a == 'P' {
				p = i
			} else {
				g = i
			}
		}
	}
	return ans + dist[m] + dist[p] + dist[g]
}
