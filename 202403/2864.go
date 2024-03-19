func maximumOddBinaryNumber(s string) string {
	one := 0
	for _, c := range s {
		if c == '1' {
			one++
		}
	}
	n := len(s)
	ans := make([]byte, n)
	ans[n-1] = '1'
	one--
	for i := 0; i < n-1; i++ {
		if one > 0 {
			ans[i] = '1'
			one--
		} else {
			ans[i] = '0'
		}
	}
	return string(ans)
}
