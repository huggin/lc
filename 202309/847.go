func shortestPathLength(graph [][]int) int {
	var q []int
	n := len(graph)

	visited := make([][]int, n)
	for i := 0; i < n; i++ {
		visited[i] = make([]int, 1<<n)
	}
	for i := 0; i < n; i++ {
		q = append(q, i, 1<<i, 0)
		visited[i][1<<i] = 1
	}

	for len(q) > 0 {
		v, mask, d := q[0], q[1], q[2]
		if mask == (1<<n)-1 {
			return d
		}
		q = q[3:]
		for _, w := range graph[v] {
			mask2 := mask | (1 << w)
			if visited[w][mask2] == 0 {
				visited[w][mask2] = 1
				q = append(q, w, mask2, d+1)
			}
		}
	}
	return -1
}
