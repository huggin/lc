import (
	"slices"

	"github.com/emirpasic/gods/queues/priorityqueue"
)

func byPriority(a, b interface{}) int {
	pa := a.([2]int)
	pb := b.([2]int)
	if pa[0] < pb[0] {
		return -1
	}
	if pa[0] > pb[0] {
		return 1
	}
	return pa[1] - pb[1]
}

func mostBooked(n int, meetings [][]int) int {
	cnt := make([]int, n)
	pq := priorityqueue.NewWith(byPriority)
	slices.SortFunc(meetings, func(a, b []int) int {
		if a[0] < b[0] {
			return -1
		}
		if a[0] > b[0] {
			return 1
		}
		return a[1] - b[1]
	})
	aval := make([]int, n)

	for _, meet := range meetings {
		for pq.Size() > 0 {
			curr, _ := pq.Peek()
			c := curr.([2]int)
			if c[0] <= meet[0] {
				aval[c[1]] = 0
				pq.Dequeue()
			} else {
				break
			}
		}
		if pq.Size() < n {
			j := -1
			for i := 0; i < n; i++ {
				if aval[i] == 0 {
					j = i
					break
				}
			}
			aval[j] = 1
			cnt[j]++
			pq.Enqueue([2]int{meet[1], j})
		} else {
			curr, _ := pq.Dequeue()
			c := curr.([2]int)
			cnt[c[1]]++
			pq.Enqueue([2]int{c[0] + meet[1] - meet[0], c[1]})
		}
	}
	ans := -1
	ma := -1
	for i := 0; i < n; i++ {
		if cnt[i] > ma {
			ma = cnt[i]
			ans = i
		}
	}
	return ans
}
