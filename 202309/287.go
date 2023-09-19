func findDuplicate(nums []int) int {
	var mark [100001]int
	for _, a := range nums {
		if mark[a] == 1 {
			return a
		}
		mark[a] = 1
	}
	return -1
}
