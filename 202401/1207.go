func uniqueOccurrences(arr []int) bool {
	f := make(map[int]int)
	for _, a := range arr {
		f[a]++
	}
	var mark [1001]int
	for _, v := range f {
		if mark[v] != 0 {
			return false
		}
		mark[v] = 1
	}
	return true
}
