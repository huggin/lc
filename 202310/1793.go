func maximumScore(nums []int, k int) int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	var st []int
	for i := 0; i < n; i++ {
		for len(st) > 0 && nums[i] <= nums[st[len(st)-1]] {
			st = st[0 : len(st)-1]
		}
		if len(st) == 0 {
			left[i] = 0
		} else {
			left[i] = st[len(st)-1] + 1
		}
		st = append(st, i)
	}

	st = []int{}
	for i := n - 1; i >= 0; i-- {
		for len(st) > 0 && nums[i] <= nums[st[len(st)-1]] {
			st = st[0 : len(st)-1]
		}
		if len(st) == 0 {
			right[i] = n - 1
		} else {
			right[i] = st[len(st)-1] - 1
		}
		st = append(st, i)
	}

	ans := 0
	for i := 0; i < n; i++ {
		if k >= left[i] && k <= right[i] {
			ans = max(ans, nums[i]*(right[i]-left[i]+1))
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
