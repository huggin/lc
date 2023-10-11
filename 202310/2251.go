import "sort"

func fullBloomFlowers(flowers [][]int, people []int) []int {
	var events [][2]int

	n := len(people)
	for _, f := range flowers {
		events = append(events, [2]int{f[0], -1})
		events = append(events, [2]int{f[1], n})
	}

	for i, p := range people {
		events = append(events, [2]int{p, i})
	}
	sort.Slice(events, func(i, j int) bool {
		return events[i][0] < events[j][0] || events[i][0] == events[j][0] && events[i][1] < events[j][1]
	})
	ans := make([]int, n)
	cnt := 0
	for _, e := range events {
		if e[1] == -1 {
			cnt++
		} else if e[1] == n {
			cnt--
		} else {
			ans[e[1]] = cnt
		}
	}
	return ans
}
