func bestClosingTime(customers string) int {
	n := len(customers)
	ans := n
	cnt := 0

	for i := n - 1; i >= 0; i-- {
		if customers[i] == 'Y' {
			cnt += 1
		} else {
			cnt -= 1
		}
		if cnt <= 0 {
			ans = i
			cnt = 0
		}
	}
	return ans
}
