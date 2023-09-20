func minOperations(nums []int, x int) int {
	n := len(nums)
	tot := 0
	for _, a := range nums {
		tot += a
	}
	tot -= x
	j := 0
	curr := 0
	ans := n + 1
	for i := 0; i < n; i++ {
		curr += nums[i]
		for j <= i && curr > tot {
			curr -= nums[j]
			j++
		}
		if curr == tot {
			ans = min(ans, n-(i-j+1))
		}
	}
	if ans == n+1 {
		return -1
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
