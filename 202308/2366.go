func minimumReplacement(nums []int) int64 {
	n := len(nums)
	var ans int64
	prev := int(1e9 + 1)
	for i := n - 1; i >= 0; i-- {
		if prev >= nums[i] {
			prev = nums[i]
		} else {
			d := (nums[i] + prev - 1) / prev
			ans += int64(d - 1)
			prev = nums[i] / d
		}
	}
	return ans
}
