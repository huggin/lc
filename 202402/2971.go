import "slices"

func largestPerimeter(nums []int) int64 {
	slices.Sort(nums)
	ans := int64(-1)
	curr := int64(nums[0]) + int64(nums[1])
	for i := 2; i < len(nums); i++ {
		if curr > int64(nums[i]) {
			ans = max(ans, curr+int64(nums[i]))
		}
		curr += int64(nums[i])
	}
	return ans
}
