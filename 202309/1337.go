import "sort"

func kWeakestRows(mat [][]int, k int) []int {
	n := len(mat)
	a := make([][2]int, 0)
	for i := 0; i < n; i++ {
		cnt := 0
		for j := 0; j < len(mat[i]); j++ {
			cnt += mat[i][j]
		}
		a = append(a, [2]int{cnt, i})
	}
	sort.Slice(a, func(i, j int) bool {
		return a[i][0] < a[j][0] || a[i][0] == a[j][0] && a[i][1] < a[j][1]
	})
	var ans []int
	for i := 0; i < k; i++ {
		ans = append(ans, a[i][1])
	}
	return ans
}
