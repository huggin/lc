func numSquares(n int) int {
	a := make([]int, n+1)
	for i := 1; i <= n; i++ {
		a[i] = -1
	}
	for i := 1; i*i <= n; i++ {
		a[i*i] = 1
	}
	var f func(k int) int
	f = func(k int) int {
		if a[k] != -1 {
			return a[k]
		}
		ans := k
		for i := 1; i*i < k; i++ {
			ans = min(ans, 1+f(k-i*i))
		}
		a[k] = ans
		return ans
	}
	return f(n)
}
