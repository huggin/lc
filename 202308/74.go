func searchMatrix(matrix [][]int, target int) bool {
	n := len(matrix)
	m := len(matrix[0])
	lo, hi := 0, n*m-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		x, y := mid/m, mid%m
		if matrix[x][y] == target {
			return true
		} else if matrix[x][y] > target {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return false
}
