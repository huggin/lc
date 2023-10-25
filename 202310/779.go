func solve(n, k int) int {
	if n == 0 && k == 0 {
		return 0
	}
	t := solve(n-1, k/2)
	if t == 0 && k%2 == 1 || t == 1 && k%2 == 0 {
		return 1
	}
	return 0
}

func kthGrammar(n int, k int) int {
	n--
	k--
	return solve(n, k)
}
