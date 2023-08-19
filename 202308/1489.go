import "sort"

type DJ struct {
	id    []int
	count []int
}

func NewDJ(n int) *DJ {
	var dj DJ
	dj.id = make([]int, n)
	dj.count = make([]int, n)
	for i := 0; i < n; i++ {
		dj.id[i] = i
	}
	return &dj
}

func (this *DJ) Find(j int) int {
	for this.id[j] != j {
		this.id[j] = this.id[this.id[j]]
		j = this.id[j]
	}
	return j
}

func (this *DJ) Union(i, j int) {
	i = this.Find(i)
	j = this.Find(j)
	if i != j {
		if this.count[i] > this.count[j] {
			this.id[j] = i
			this.count[i] += this.count[j]
		} else {
			this.id[i] = j
			this.count[j] += this.count[i]
		}
	}
}

func kruskal(n int, edge [][]int, index int, force bool) int {
	dj := NewDJ(n)
	ans := 0
	cnt := 0
	if index != -1 && force {
		dj.Union(edge[index][1], edge[index][2])
		ans += edge[index][0]
		cnt++
	}
	for k, e := range edge {
		if k == index {
			continue
		}
		i := e[1]
		j := e[2]
		if dj.Find(i) != dj.Find(j) {
			dj.Union(i, j)
			cnt++
			ans += e[0]
		}
		if cnt == n-1 {
			return ans
		}
	}
	return -1
}

func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
	ewi := make([][]int, len(edges))
	for i, e := range edges {
		ewi[i] = make([]int, 4)
		ewi[i][0] = e[2]
		ewi[i][1] = e[0]
		ewi[i][2] = e[1]
		ewi[i][3] = i
	}
	sort.Slice(ewi, func(i, j int) bool {
		if ewi[i][0] < ewi[j][0] {
			return true
		}
		return false
	})
	mst := kruskal(n, ewi, -1, false)

	ans := make([][]int, 2)
	for i, e := range ewi {
		mst2 := kruskal(n, ewi, i, true)
		mst3 := kruskal(n, ewi, i, false)
		if mst3 == -1 || mst3 > mst {
			ans[0] = append(ans[0], e[3])
		} else if mst2 == mst {
			ans[1] = append(ans[1], e[3])
		}
	}
	return ans
}
