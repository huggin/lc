func permute(nums []int) [][]int {
	var ans [][]int
	n := len(nums)
	var curr []int

	var dfs func(k int)
	dfs = func(k int) {
		if k == n {
			res := make([]int, n)
			copy(res, curr)
			ans = append(ans, res)
			return
		}
		for i := k; i < n; i++ {
			nums[i], nums[k] = nums[k], nums[i]
			curr = append(curr, nums[k])
			dfs(k + 1)
			curr = curr[0 : len(curr)-1]
			nums[i], nums[k] = nums[k], nums[i]
		}
	}

	dfs(0)
	return ans
}
