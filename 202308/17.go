func letterCombinations(digits string) []string {
	a := []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
	curr := ""
	n := len(digits)
	ans := make([]string, 0)
	if n == 0 {
		return ans
	}

	var f func(k int)
	f = func(k int) {
		if k == n {
			ans = append(ans, curr)
			return
		}
		for i := 0; i < len(a[digits[k]-'0']); i++ {
			curr += string(a[digits[k]-'0'][i])
			f(k + 1)
			curr = curr[0 : len(curr)-1]
		}
	}

	f(0)
	return ans
}
