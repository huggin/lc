import "slices"

func reductionOperations(nums []int) int {
	slices.Sort(nums)
	cnt := 0
	prev := nums[0]
	ans := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] > prev {
			cnt++
		}
		ans += cnt
		prev = nums[i]
	}
	return ans
}
