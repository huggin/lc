func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
	if t == 1 && sx == fx && sy == fy {
		return false
	}
	steps := max(abs(sx-fx), abs(sy-fy))
	if steps > t {
		return false
	}
	return true
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}
