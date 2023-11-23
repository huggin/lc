import "slices"

func check(a []int) bool {
	n := len(a)
	if n <= 2 {
		return true
	}
	d := a[1] - a[0]
	for i := 2; i < n; i++ {
		if a[i]-a[i-1] != d {
			return false
		}
	}
	return true
}

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	n := len(l)
	ans := make([]bool, n)
	for k := range l {
		a := slices.Clone(nums[l[k] : r[k]+1])
		slices.Sort(a)
		ans[k] = check(a)
	}
	return ans
}
