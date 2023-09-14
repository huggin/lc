import "sort"

func findItinerary(tickets [][]string) []string {
	var ans []string
	ans = append(ans, "JFK")
	g := make(map[string][]string)
	var mark map[string]int

	for _, tick := range tickets {
		g[tick[0]] = append(g[tick[0]], tick[1])
	}
	for k := range g {
		sort.Strings(g[k])
	}

	var dfsCount func(v string) int
	dfsCount = func(v string) int {
		mark[v] = 1
		cnt := 1
		for _, w := range g[v] {
			if w != "$$$" && mark[w] == 0 {
				cnt += dfsCount(w)
			}
		}
		return cnt
	}

	isValid := func(v, w string, k int) bool {
		cnt := 0
		for i := range g[v] {
			if g[v][i] != "$$$" {
				cnt++
			}
		}
		if cnt == 1 {
			return true
		}

		mark = make(map[string]int)
		cnt1 := dfsCount(v)
		g[v][k] = "$$$"
		mark = make(map[string]int)
		cnt2 := dfsCount(w)
		g[v][k] = w
		return cnt1 == cnt2
	}

	var dfs func(v string)
	dfs = func(v string) {
		for k, w := range g[v] {
			if g[v][k] != "$$$" && isValid(v, w, k) {
				ans = append(ans, w)
				g[v][k] = "$$$"
				dfs(w)
				break
			}
		}
	}
	dfs("JFK")

	return ans
}
