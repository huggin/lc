func sortItems(n int, m int, group []int, beforeItems [][]int) []int {
	gr := make(map[int]map[int]bool)
	for i, v := range group {
		if v == -1 {
			continue
		}
		if _, ok := gr[v]; !ok {
			gr[v] = make(map[int]bool)
		}
		gr[v][i] = true
	}

	g := make([][]int, n)
	for i := 0; i < n; i++ {
		for _, from := range beforeItems[i] {
			if group[from] == group[i] || group[from] == -1 {
				g[from] = append(g[from], i)
			} else {
				for f := range gr[group[from]] {
					g[f] = append(g[f], i)
				}
			}
		}
	}

	marked := make([]bool, n)
	stack := make([]bool, n)
	found := false

	var topo []int

	var dfs func(v int, f *bool)
	dfs = func(v int, f *bool) {
		marked[v] = true
		stack[v] = true
		for _, w := range g[v] {
			if !marked[w] {
				dfs(w, f)
			} else if stack[w] {
				*f = true
			}
		}
		stack[v] = false
		topo = append(topo, v)
	}

	for i := 0; i < n; i++ {
		if !marked[i] {
			dfs(i, &found)
		}
	}
	if found {
		return make([]int, 0)
	}

	ans := make([][]int, 0)
	marked = make([]bool, n)
	mg := make([]int, m)
	for i := 0; i < m; i++ {
		mg[i] = -1
	}

	for i := 0; i < n; i++ {
		if group[topo[i]] == -1 {
			temp := make([]int, 0)
			temp = append(temp, topo[i])
			ans = append(ans, temp)
		} else if mg[group[topo[i]]] == -1 {
			temp := make([]int, 0)
			temp = append(temp, topo[i])
			ans = append(ans, temp)
			mg[group[topo[i]]] = len(ans) - 1
		} else {
			ans[mg[group[topo[i]]]] = append(ans[mg[group[topo[i]]]], topo[i])
		}
	}

	var res []int
	for i := len(ans) - 1; i >= 0; i-- {
		for j := len(ans[i]) - 1; j >= 0; j-- {
			res = append(res, ans[i][j])
		}
	}

	return res
}
