func minimumTime(n int, relations [][]int, time []int) int {
	g := make([][]int, n)
	for _, e := range relations {
		g[e[0]-1] = append(g[e[0]-1], e[1]-1)
	}

	var topo []int
	visited := make([]int, n)

	var dfs func(u int)
	dfs = func(u int) {
		visited[u] = 1
		for _, v := range g[u] {
			if visited[v] == 0 {
				dfs(v)
			}
		}
		topo = append(topo, u)
	}

	for i := 0; i < n; i++ {
		if visited[i] == 0 {
			dfs(i)
		}
	}
	ans := 0
	dp := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		dp[topo[i]] += time[topo[i]]
		ans = max(dp[topo[i]], ans)
		for _, j := range g[topo[i]] {
			dp[j] = max(dp[j], dp[topo[i]])
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
