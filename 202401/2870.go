func minOperations(nums []int) int {
	cnt := make(map[int]int)
	for _, a := range nums {
		cnt[a]++
	}
	ans := 0
	for _, v := range cnt {
		if v == 1 {
			return -1
		}
		ans += (v + 2) / 3
	}
	return ans
}
