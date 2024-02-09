import "slices"

func largestDivisibleSubset(nums []int) []int {
	slices.Sort(nums)
	n := len(nums)
	dp := make([]int, n)
	prev := make([]int, n)
	ans := 0
	last := -1
	for i := 0; i < n; i++ {
		dp[i] = 1
		prev[i] = -1
		for j := 0; j < i; j++ {
			if nums[i]%nums[j] == 0 {
				if dp[j]+1 > dp[i] {
					dp[i] = dp[j] + 1
					prev[i] = j
				}
			}
		}
		if ans < dp[i] {
			ans = dp[i]
			last = i
		}
	}
	var res []int
	for i := last; i != -1; i = prev[i] {
		res = append(res, nums[i])
	}
	return res
}
