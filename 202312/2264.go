func largestGoodInteger(num string) string {
	var ans string
	n := len(num)
	for i := 2; i < n; i++ {
		if num[i] == num[i-1] && num[i] == num[i-2] && ans < num[i-2:i+1] {
			ans = num[i-2 : i+1]
		}
	}
	return ans
}
