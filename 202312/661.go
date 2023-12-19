func imageSmoother(img [][]int) [][]int {
	n := len(img)
	m := len(img[0])
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		ans[i] = make([]int, m)
	}
	dx := []int{-1, -1, -1, 0, 0, 1, 1, 1}
	dy := []int{-1, 0, 1, -1, 1, -1, 0, 1}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			total := img[i][j]
			cnt := 1
			for k := 0; k < 8; k++ {
				ni := i + dx[k]
				nj := j + dy[k]
				if ni >= 0 && ni < n && nj >= 0 && nj < m {
					total += img[ni][nj]
					cnt++
				}
			}
			ans[i][j] = total / cnt
		}
	}
	return ans
}
