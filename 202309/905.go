import "sort"

func sortArrayByParity(nums []int) []int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i]%2 == 0 && nums[j]%2 == 1
	})
	return nums
}
