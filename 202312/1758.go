func minOperations(s string) int {
	return min(f(s, true), f(s, false))
}

func f(s string, curr bool) int {
	n := len(s)
	ans := 0
	for i := 0; i < n; i++ {
		if curr && s[i] == '1' || !curr && s[i] == '0' {
			ans++
		}
		curr = !curr
	}
	return ans
}
