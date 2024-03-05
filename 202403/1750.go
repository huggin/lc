func minimumLength(s string) int {
	n := len(s)
	i, j := 0, n-1
	for i < j {
		if s[i] == s[j] {
			for i+1 < j && s[i] == s[i+1] {
				i++
			}
			for i < j-1 && s[j-1] == s[j] {
				j--
			}
			i++
			j--
		} else {
			break
		}
	}
	if i > j {
		return 0
	}
	return j - i + 1
}
