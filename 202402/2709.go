func canTraverseAllPairs(nums []int) bool {
	n := len(nums)
	if n == 1 {
		return true
	}
	curr := n
	p2i := make(map[int]int)
	g := make([][]int, n)
	for i := 0; i < n; i++ {
		g[i] = make([]int, 0)
	}
	seen := make(map[int]bool)
	for j, a := range nums {
		if seen[a] {
			continue
		}
		seen[a] = true

		for i := 2; i*i <= a; i++ {
			if a%i == 0 {
				for a%i == 0 {
					a /= i
				}
				if _, ok := p2i[i]; !ok {
					p2i[i] = curr
					curr++
					g = append(g, []int{})
				}
				g[p2i[i]] = append(g[p2i[i]], j)
				g[j] = append(g[j], p2i[i])
			}
		}
		if a != 1 {
			if _, ok := p2i[a]; !ok {
				p2i[a] = curr
				curr++
				g = append(g, []int{})
			}
			g[p2i[a]] = append(g[p2i[a]], j)
			g[j] = append(g[j], p2i[a])
		}
	}

	m := len(g)
	visited := make([]int, m)
	visited[0] = 1
	q := []int{0}
	for len(q) > 0 {
		curr = q[0]
		q = q[1:]
		for _, v := range g[curr] {
			if visited[v] == 0 {
				visited[v] = 1
				q = append(q, v)
			}
		}
	}
	seen = make(map[int]bool)
	for i := 0; i < n; i++ {
		if nums[i] == 1 || visited[i] == 0 && seen[nums[i]] == false {
			return false
		}
		seen[nums[i]] = true
	}

	return true
}
