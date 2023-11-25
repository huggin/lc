func getSumAbsoluteDifferences(nums []int) []int {
	n := len(nums)
	pre := make([]int, n)
	suf := make([]int, n)
	pre[0] = nums[0]
	for i := 1; i < n; i++ {
		pre[i] = pre[i-1] + nums[i]
	}
	suf[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		suf[i] = suf[i+1] + nums[i]
	}
	ans := make([]int, n)
	ans[0] = suf[1] - (n-1)*nums[0]
	ans[n-1] = (n-1)*nums[n-1] - pre[n-2]
	for i := 1; i < n-1; i++ {
		ans[i] = suf[i+1] - (n-i-1)*nums[i] + i*nums[i] - pre[i-1]
	}
	return ans
}
