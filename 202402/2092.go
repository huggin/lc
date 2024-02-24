import "sort"

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	g := make(map[int]map[int][]int)
	var time []int
	visited := make([]int, n)

	for _, e := range meetings {
		time = append(time, e[2])
		if _, ok := g[e[2]]; !ok {
			g[e[2]] = make(map[int][]int)
		}
		g[e[2]][e[0]] = append(g[e[2]][e[0]], e[1])
		g[e[2]][e[1]] = append(g[e[2]][e[1]], e[0])
	}
	sort.Ints(time)
	secret := make(map[int]bool)
	secret[0] = true
	secret[firstPerson] = true
	for i := 0; i < len(time); i++ {
		if i != 0 && time[i] == time[i-1] {
			continue
		}
		gc := g[time[i]]
		q := []int{}

		for k := range gc {
			if secret[k] {
				visited[k] = 1
				q = append(q, k)
			} else {
				visited[k] = 0
			}
		}

		for len(q) > 0 {
			curr := q[0]
			q = q[1:]
			for _, v := range gc[curr] {
				if visited[v] == 0 {
					visited[v] = 1
					secret[v] = true
					q = append(q, v)
				}
			}
		}
	}
	var ans []int
	for k := range secret {
		ans = append(ans, k)
	}
	return ans
}
