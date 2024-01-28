func count(a []int, target int) int {
	hash := make(map[int]int)
	n := len(a)
	hash[0] = 1
	ans := 0
	total := 0
	for i := 0; i < n; i++ {
		total += a[i]
		ans += hash[total-target]
		hash[total]++
	}
	return ans
}

func numSubmatrixSumTarget(matrix [][]int, target int) int {
	n := len(matrix)
	m := len(matrix[0])
	ans := 0
	for i := 0; i < n; i++ {
		ans += count(matrix[i], target)
	}
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		a[i] = make([]int, m)
		copy(a[i], matrix[i])
	}

	for i := 1; i < n; i++ {
		for k := 0; k+i < n; k++ {
			for j := 0; j < m; j++ {
				a[k][j] += matrix[k+i][j]
			}
			ans += count(a[k], target)
		}
	}
	return ans
}
