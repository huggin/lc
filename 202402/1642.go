import (
	"github.com/emirpasic/gods/queues/priorityqueue"
	"github.com/emirpasic/gods/utils"
)

func furthestBuilding(heights []int, bricks int, ladders int) int {
	q := priorityqueue.NewWith(utils.IntComparator)
	n := len(heights)
	total := 0
	for i := 1; i < n; i++ {
		d := heights[i] - heights[i-1]
		if d > 0 {
			if q.Size() < ladders {
				q.Enqueue(d)
			} else {
				least, ok := q.Peek()
				if !ok || least.(int) >= d {
					total += d
				} else {
					total += least.(int)
					q.Dequeue()
					q.Enqueue(d)
				}
			}
			if total > bricks {
				return i - 1
			}
		}
	}
	return n - 1
}
