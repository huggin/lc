import "sort"

func numFactoredBinaryTrees(arr []int) int {
	dp := make(map[int]int)
	sort.Ints(arr)
	n := len(arr)

	for i := 0; i < n; i++ {
		dp[arr[i]]++
	}
	mod := int(1e9 + 7)

	var ans int
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if arr[i]%arr[j] != 0 {
				continue
			}
			d := arr[i] / arr[j]
			if _, ok := dp[d]; ok {
				dp[arr[i]] = (dp[arr[i]] + dp[arr[j]]*dp[d]) % mod
			}
		}
		ans = (ans + dp[arr[i]]) % mod
	}

	return ans
}
