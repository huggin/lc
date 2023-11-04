func buildArray(target []int, n int) []string {
	var ans []string

	j := 0
	for i := 1; i <= n && j < len(target); i++ {
		if target[j] != i {
			ans = append(ans, "Push", "Pop")
		} else {
			ans = append(ans, "Push")
			j++
		}
	}
	return ans
}
