import "slices"

func minPairSum(nums []int) int {
	slices.Sort(nums)
	ans := 0
	n := len(nums)
	for i := 0; i < n/2; i++ {
		ans = max(ans, nums[i]+nums[n-1-i])
	}
	return ans
}
