import (
	pq "github.com/emirpasic/gods/queues/priorityqueue"
	"github.com/emirpasic/gods/utils"
)

type Edge struct {
	from   int
	to     int
	weight int
}

type Element struct {
	weight int
	node   int
}

func byPriority(a, b interface{}) int {
	wa := a.(Element).weight
	wb := b.(Element).weight
	return utils.IntComparator(wa, wb)
}

type Graph struct {
	adj [][]Edge
	n   int
}

func Constructor(n int, edges [][]int) Graph {
	var g Graph
	g.n = n
	g.adj = make([][]Edge, n)
	for _, e := range edges {
		g.adj[e[0]] = append(g.adj[e[0]], Edge{e[0], e[1], e[2]})
	}
	return g
}

func (this *Graph) AddEdge(edge []int) {
	this.adj[edge[0]] = append(this.adj[edge[0]], Edge{edge[0], edge[1], edge[2]})
}

func (this *Graph) ShortestPath(node1 int, node2 int) int {
	q := pq.NewWith(byPriority)
	dist := make([]int, this.n)
	for i := 0; i < this.n; i++ {
		dist[i] = -1
	}
	dist[node1] = 0
	q.Enqueue(Element{0, node1})
	for !q.Empty() {
		front, _ := q.Dequeue()
		curr := front.(Element)
		dist[curr.node] = curr.weight
		if curr.node == node2 {
			break
		}
		for _, e := range this.adj[curr.node] {
			if dist[e.to] == -1 || dist[e.to] > curr.weight+e.weight {
				dist[e.to] = curr.weight + e.weight
				q.Enqueue(Element{dist[e.to], e.to})
			}
		}
	}
	return dist[node2]
}

/**
 * Your Graph object will be instantiated and called as such:
 * obj := Constructor(n, edges);
 * obj.AddEdge(edge);
 * param_2 := obj.ShortestPath(node1,node2);
 */
