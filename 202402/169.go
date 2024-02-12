func majorityElement(nums []int) int {
	n := len(nums)
	cnt := make(map[int]int)
	for i := 0; i < n; i++ {
		cnt[nums[i]]++
	}
	for k, v := range cnt {
		if v > n/2 {
			return k
		}
	}
	return -1
}
