func numBusesToDestination(routes [][]int, source int, target int) int {
	visited := make([]int, 1000000)
	var q []int
	n := len(routes)
	visited2 := make([]int, n)

	rs := make([]map[int]bool, n)
	for k, r := range routes {
		rs[k] = make(map[int]bool)
		for _, a := range r {
			rs[k][a] = true
		}
	}

	visited[source] = 1
	q = append(q, source, 0)

	for len(q) > 0 {
		curr := q[0]
		dist := q[1]

		if curr == target {
			return dist
		}
		q = q[2:]
		for i := 0; i < n; i++ {
			if rs[i][curr] == true && visited2[i] == 0 {
				visited2[i] = 1
				for j := 0; j < len(routes[i]); j++ {
					if routes[i][j] == curr || visited[routes[i][j]] == 1 {
						continue
					}
					visited[routes[i][j]] = 1
					q = append(q, routes[i][j], dist+1)
				}
			}
		}
	}
	return -1
}
