func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
	deg := make([]int, n)
	for i := 0; i < n; i++ {
		if leftChild[i] != -1 {
			deg[leftChild[i]]++
		}
		if rightChild[i] != -1 {
			deg[rightChild[i]]++
		}
	}
	root := 0
	for i := 0; i < n; i++ {
		if deg[i] > 1 {
			return false
		}
		if deg[i] == 0 {
			root++
		}
	}
	if root != 1 {
		return false
	}

	var topo []int
	visited := make([]int, n)

	var dfs func(int)
	dfs = func(u int) {
		visited[u] = 1
		if leftChild[u] != -1 && visited[leftChild[u]] == 0 {
			dfs(leftChild[u])
		}
		if rightChild[u] != -1 && visited[rightChild[u]] == 0 {
			dfs(rightChild[u])
		}
		topo = append(topo, u)
	}

	for i := 0; i < n; i++ {
		if visited[i] == 0 {
			dfs(i)
		}
	}

	visited = make([]int, n)
	var dfs2 func(int)
	dfs2 = func(u int) {
		visited[u] = 1
		if leftChild[u] != -1 && visited[leftChild[u]] == 0 {
			dfs(leftChild[u])
		}
		if rightChild[u] != -1 && visited[rightChild[u]] == 0 {
			dfs(rightChild[u])
		}
	}

	cnt := 0
	for i := n - 1; i >= 0; i-- {
		if visited[topo[i]] == 0 {
			cnt++
			dfs2(topo[i])
		}
	}
	return cnt == 1
}
