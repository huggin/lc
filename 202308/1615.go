func maximalNetworkRank(n int, roads [][]int) int {
	ans := 0
	g := make([]int, n)
	edges := make(map[int]int)

	for _, edge := range roads {
		g[edge[0]]++
		g[edge[1]]++
		a, b := edge[0], edge[1]
		if a > b {
			a, b = b, a
		}
		edges[a*n+b] = 1
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			temp := g[i] + g[j]
			if _, ok := edges[i*n+j]; ok {
				temp -= 1
			}
			ans = max(ans, temp)
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
