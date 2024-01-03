func numberOfBeams(bank []string) int {
	n := len(bank)
	m := len(bank[0])
	cnt := make([]int, n)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if bank[i][j] == '1' {
				cnt[i]++
			}
		}
	}
	ans := 0
	j := -1
	for i := 0; i < n; i++ {
		if cnt[i] != 0 {
			if j != -1 {
				ans += cnt[i] * cnt[j]
			}
			j = i
		}
	}
	return ans
}
