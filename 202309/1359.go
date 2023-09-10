func countOrders(n int) int {
	ans := 1
	m := int(1e9 + 7)
	for i := 1; i <= 2*n; i++ {
		if i%2 == 0 {
			ans = ans * (i / 2) % m
		} else {
			ans = ans * i % m
		}
	}
	return ans
}
