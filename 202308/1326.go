import "sort"

func minTaps(n int, ranges []int) int {
	dp := make([][101]int, n+1)
	for i := 0; i < n; i++ {
		for j := 0; j < 101; j++ {
			dp[i][j] = -1
		}
	}

	a := make([][2]int, n+1)
	for i := 0; i <= n; i++ {
		a[i][0] = i - ranges[i]
		a[i][1] = i + ranges[i]
	}

	sort.Slice(a, func(i, j int) bool {
		if a[i][0] < a[j][0] || a[i][0] == a[j][0] && a[i][1] < a[j][1] {
			return true
		}
		return false
	})

	ans := 0
	prev := 0
	next := -1
	for i := 0; i <= n; {
		if a[i][0] > prev {
			return -1
		} else {
			for i <= n && a[i][0] <= prev {
				next = max(next, a[i][1])
				i++
			}
			ans++
			if next >= n {
				return ans
			} else {
				prev = next
			}
		}
	}
	if next >= n {
		return ans
	}
	return -1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
