func knightDialer(n int) int {
	dx := [8]int{-2, -2, -1, -1, 1, 1, 2, 2}
	dy := [8]int{-1, 1, -2, 2, -2, 2, -1, 1}
	var dp [5001][10]int
	const MOD = int(1e9 + 7)
	for i := 0; i < 10; i++ {
		dp[0][i] = 1
	}
	b := [4][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {-1, 0, -1}}
	pos := [10][2]int{{3, 1}, {0, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1}, {1, 2}, {2, 0}, {2, 1}, {2, 2}}
	for i := 1; i < n; i++ {
		for j := 0; j < 10; j++ {
			x := pos[j][0]
			y := pos[j][1]

			for k := 0; k < 8; k++ {
				nx := x + dx[k]
				ny := y + dy[k]
				if nx >= 0 && nx < 4 && ny >= 0 && ny < 3 && b[nx][ny] != -1 {
					dp[i][b[nx][ny]] = (dp[i][b[nx][ny]] + dp[i-1][j]) % MOD
				}
			}
		}
	}
	ans := 0
	for i := 0; i < 10; i++ {
		ans = (ans + dp[n-1][i]) % MOD
	}
	return ans
}
