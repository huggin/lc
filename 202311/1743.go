func restoreArray(adjacentPairs [][]int) []int {
	n := len(adjacentPairs)
	g := make(map[int][]int)
	deg := make(map[int]int)
	for _, a := range adjacentPairs {
		deg[a[0]]++
		deg[a[1]]++
		g[a[0]] = append(g[a[0]], a[1])
		g[a[1]] = append(g[a[1]], a[0])
	}
	visited := make(map[int]int)
	var ans []int
	for k, v := range deg {
		if v == 1 {
			ans = append(ans, k)
			visited[k] = 1
			break
		}
	}
	for len(ans) < n+1 {
		for i := 0; i < len(g[ans[len(ans)-1]]); i++ {
			if visited[g[ans[len(ans)-1]][i]] == 0 {
				visited[g[ans[len(ans)-1]][i]] = 1
				ans = append(ans, g[ans[len(ans)-1]][i])
			}
		}
	}

	return ans
}
