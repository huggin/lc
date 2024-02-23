type Node struct {
	dest int
	stop int
	u    int
}

func byDest(a, b interface{}) int {
	stopA := a.(Node).stop
	stopB := b.(Node).stop
	if stopA < stopB {
		return -1
	} else if stopA > stopB {
		return 1
	}
	destA := a.(Node).dest
	destB := b.(Node).dest
	return utils.IntComparator(destA, destB)
}

func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	adj := make([][][2]int, n)
	for _, f := range flights {
		adj[f[0]] = append(adj[f[0]], [2]int{f[1], f[2]})
	}
	pq := priorityqueue.NewWith(byDest)
	pq.Enqueue(Node{0, 0, src})
	dest := make([]int, n)
	for i := 0; i < n; i++ {
		dest[i] = -1
	}
	dest[src] = 0
	for pq.Size() > 0 {
		curr, _ := pq.Dequeue()
		currDest := curr.(Node).dest
		currStop := curr.(Node).stop
		u := curr.(Node).u
		if dest[u] == -1 || currDest < dest[u] {
			dest[u] = currDest
		}
		if currStop <= k {
			for _, v := range adj[u] {
				if dest[v[0]] == -1 || dest[v[0]] > currDest+v[1] {
					pq.Enqueue(Node{currDest + v[1], currStop + 1, v[0]})
				}
			}
		}
	}

	return dest[dst]
}
