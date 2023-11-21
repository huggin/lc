func countNicePairs(nums []int) int {
	m := make(map[int]int)
	ans := int64(0)

	f := func(n int) int {
		if n < 10 {
			return n
		}

		for n%10 == 0 {
			n /= 10
		}
		ans := 0
		for n > 0 {
			ans = ans*10 + n%10
			n /= 10
		}
		return ans
	}

	for _, a := range nums {
		d := a - f(a)
		m[d]++
	}
	for _, v := range m {
		ans = (ans + int64(v)*int64(v-1)/2)
	}
	return int(ans % 1000000007)
}
