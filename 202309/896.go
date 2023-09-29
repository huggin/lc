import "sort"

func isMonotonic(nums []int) bool {
	ans := sort.SliceIsSorted(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	if ans {
		return true
	}
	return sort.SliceIsSorted(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})
}
