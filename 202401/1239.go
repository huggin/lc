func maxLength(arr []string) int {
	n := len(arr)
	mask := make([]int, n)
	for i, s := range arr {
		for _, c := range s {
			if (mask[i] & (1 << (c - 'a'))) != 0 {
				mask[i] = 0
				break
			} else {
				mask[i] |= (1 << (c - 'a'))
			}
		}
	}

	ans := 0
	var curr []byte
	var f func(k int, m int)
	f = func(k int, m int) {
		if k == n {
			ans = max(ans, len(curr))
			return
		}
		f(k+1, m)
		for i := k; i < n; i++ {
			if mask[i] != 0 && (mask[i]&m) == 0 {
				curr = append(curr, []byte(arr[i])...)
				f(i+1, m|mask[i])
				curr = curr[0 : len(curr)-len(arr[i])]
			}
		}
	}
	f(0, 0)
	return ans
}
