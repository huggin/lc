func candy(ratings []int) int {
	n := len(ratings)
	candy := make([]int, n)
	for i := 0; i < n; i++ {
		candy[i] = 1
	}
	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i-1] {
			candy[i] = candy[i-1] + 1
		}
	}
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			candy[i] = max(candy[i], candy[i+1]+1)
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		ans += candy[i]
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
