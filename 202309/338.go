func cnt(n int) int {
	ans := 0
	for n > 0 {
		ans++
		n &= n - 1
	}
	return ans
}

func countBits(n int) []int {
	ans := make([]int, n+1)
	for i := 0; i <= n; i++ {
		ans[i] = cnt(i)
	}
	return ans
}
