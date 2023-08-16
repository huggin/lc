func maxSlidingWindow(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)
	q := make([]int, 0)
	for i := 0; i < k; i++ {
		for len(q) > 0 && q[len(q)-1] < nums[i] {
			q = q[0 : len(q)-1]
		}
		q = append(q, nums[i])

	}
	ans[0] = q[0]
	for i := k; i < n; i++ {
		if q[0] == nums[i-k] {
			q = q[1:]
		}
		for len(q) > 0 && q[len(q)-1] < nums[i] {
			q = q[0 : len(q)-1]
		}

		q = append(q, nums[i])

		ans[i-k+1] = q[0]
	}
	return ans
}
