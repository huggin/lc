import "slices"

func maxProductDifference(nums []int) int {
	slices.Sort(nums)
	n := len(nums)
	return nums[n-1]*nums[n-2] - nums[0]*nums[1]
}
