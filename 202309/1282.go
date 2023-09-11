func groupThePeople(groupSizes []int) [][]int {
	m := make(map[int][]int)
	for i, a := range groupSizes {
		m[a] = append(m[a], i)
	}
	ans := make([][]int, 0)
	for k, v := range m {
		for i := 0; i < len(v); i += k {
			var temp []int
			for j := i; j < i+k; j++ {
				temp = append(temp, v[j])
			}
			ans = append(ans, temp)
		}
	}
	return ans
}
