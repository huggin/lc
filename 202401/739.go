func dailyTemperatures(t []int) []int {
	st := make([]int, 0)
	n := len(t)
	ans := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		for len(st) > 0 && t[st[len(st)-1]] <= t[i] {
			st = st[0 : len(st)-1]
		}
		if len(st) != 0 {
			ans[i] = st[len(st)-1] - i
		}
		st = append(st, i)
	}
	return ans
}
