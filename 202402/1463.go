func cherryPickup(grid [][]int) int {
	n := len(grid)
	m := len(grid[0])
	var dp [70][70][70]int
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < m; k++ {
				dp[i][j][k] = -1
			}
		}
	}
	d := [3]int{-1, 0, 1}

	var f func(i, j, k int) int
	f = func(i, j, k int) int {
		if i == n || j >= k {
			return 0
		}
		if dp[i][j][k] != -1 {
			return dp[i][j][k]
		}
		ans := grid[i][j] + grid[i][k]
		temp := 0
		for jj := 0; jj < 3; jj++ {
			for kk := 0; kk < 3; kk++ {
				if j+d[jj] >= 0 && k+d[kk] < m {
					temp = max(temp, f(i+1, j+d[jj], k+d[kk]))
				}
			}
		}
		dp[i][j][k] = temp + ans
		return dp[i][j][k]
	}

	return f(0, 0, m-1)
}
