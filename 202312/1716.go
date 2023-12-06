func totalMoney(n int) int {
	ans := 0
	one := 0
	for i := 1; i <= n; i++ {
		if (i-1)%7 == 0 {
			one++
		}
		ans += one + (i-1)%7
	}
	return ans
}
