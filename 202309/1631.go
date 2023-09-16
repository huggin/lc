import (
	pq "github.com/emirpasic/gods/queues/priorityqueue"
	"github.com/emirpasic/gods/utils"
)

type Element struct {
	dist int
	x    int
	y    int
}

func byDist(a, b interface{}) int {
	dista := a.(Element).dist
	distb := b.(Element).dist
	return utils.IntComparator(dista, distb)
}

func minimumEffortPath(heights [][]int) int {
	dx := [4]int{-1, 0, 0, 1}
	dy := [4]int{0, -1, 1, 0}
	queue := pq.NewWith(byDist)
	n := len(heights)
	m := len(heights[0])
	dst := make([][]int, n)
	for i := 0; i < n; i++ {
		dst[i] = make([]int, m)
		for j := 0; j < m; j++ {
			dst[i][j] = 99999999
		}
	}

	dst[0][0] = 0
	queue.Enqueue(Element{0, 0, 0})

	for !queue.Empty() {
		v, _ := queue.Dequeue()
		e := v.(Element)
		d, x, y := e.dist, e.x, e.y
		if x == n-1 && y == m-1 {
			break
		}
		for k := 0; k < 4; k++ {
			nx := x + dx[k]
			ny := y + dy[k]
			if !(nx >= 0 && nx < n && ny >= 0 && ny < m) {
				continue
			}

			nd := max(d, abs(heights[x][y]-heights[nx][ny]))

			if nd < dst[nx][ny] {
				dst[nx][ny] = nd
				queue.Enqueue(Element{nd, nx, ny})
			}
		}
	}

	return dst[n-1][m-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
