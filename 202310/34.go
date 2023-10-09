import "sort"

func searchRange(nums []int, target int) []int {
	idx := sort.SearchInts(nums, target)
	if idx == len(nums) || nums[idx] != target {
		return []int{-1, -1}
	}
	idx2 := sort.Search(len(nums), func(i int) bool {
		return nums[i] > target
	})
	return []int{idx, idx2 - 1}
}
