import "sort"

func minOperations(nums []int) int {
	sort.Ints(nums)
	var a []int
	n := len(nums)
	for i := 0; i < n; i++ {
		if len(a) == 0 || a[len(a)-1] != nums[i] {
			a = append(a, nums[i])
		}
	}
	ans := n - 1
	for i := 0; i < len(a); i++ {
		j := sort.SearchInts(a, a[i]+n-1)
		if j != len(a) && a[j] == a[i]+n-1 {
			ans = min(ans, n-(j-i+1))
		} else {
			ans = min(ans, n-(j-i))
		}
	}

	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
