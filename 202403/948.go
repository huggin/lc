import "slices"

func bagOfTokensScore(tokens []int, power int) int {
	slices.Sort(tokens)
	n := len(tokens)
	ans := 0
	score := 0

	for i, j := 0, n-1; i <= j; {
		if power >= tokens[i] {
			score++
			power -= tokens[i]
			i++
			ans = max(score, ans)
		} else if score > 0 {
			score--
			power += tokens[j]
			j--
		} else {
			break
		}
	}
	return ans
}
