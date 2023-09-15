import "sort"

func minCostConnectPoints(points [][]int) int {
	n := len(points)
	var edge [][3]int
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			e := [3]int{abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j}
			edge = append(edge, e)
		}
	}
	sort.Slice(edge, func(i, j int) bool {
		return edge[i][0] < edge[j][0]
	})

	id := make([]int, n)
	for i := 0; i < n; i++ {
		id[i] = i
	}
	count := make([]int, n)
	for i := 0; i < n; i++ {
		count[i] = 1
	}

	find := func(i int) int {
		for id[i] != i {
			id[i] = id[id[i]]
			i = id[i]
		}
		return i
	}

	union := func(i, j int) {
		i = find(i)
		j = find(j)
		if count[i] < count[j] {
			id[i] = j
			count[j] += count[i]
		} else {
			id[j] = i
			count[i] += count[j]
		}
	}

	ans := 0
	m := 0
	for _, e := range edge {
		u := find(e[1])
		v := find(e[2])
		if u != v {
			m++
			ans += e[0]
			union(e[1], e[2])
		}
		if m == n-1 {
			break
		}
	}
	return ans
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
