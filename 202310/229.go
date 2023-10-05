func majorityElement(nums []int) []int {
	n := len(nums)
	cnt := make(map[int]int)
	for _, a := range nums {
		cnt[a]++
	}
	var ans []int
	for k, v := range cnt {
		if v > n/3 {
			ans = append(ans, k)
		}
	}
	return ans
}
