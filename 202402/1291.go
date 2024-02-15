import "slices"

func sequentialDigits(low int, high int) []int {
	ans := make([]int, 0)
	q := make([]int, 0)
	for i := 1; i <= 9; i++ {
		q = append(q, i)
	}
	for len(q) > 0 {
		c := q[0]
		q = q[1:]
		if c >= low && c <= high {
			ans = append(ans, c)
		} else if c > high {
			continue
		}
		d := c % 10
		if d != 9 {
			q = append(q, c*10+d+1)
		}
	}
	slices.Sort(ans)
	return ans
}
