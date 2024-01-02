func findMatrix(nums []int) [][]int {
	cnt := make(map[int]int)
	for _, a := range nums {
		cnt[a]++
	}
	row := 0
	for _, v := range cnt {
		row = max(row, v)
	}
	ans := make([][]int, row)
	for i := 0; i < row; i++ {
		ans[i] = make([]int, 0)
	}
	for k, v := range cnt {
		for i := 0; i < v; i++ {
			ans[i] = append(ans[i], k)
		}
	}
	return ans
}
