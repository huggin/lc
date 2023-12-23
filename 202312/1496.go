func isPathCrossing(path string) bool {
	v := make(map[[2]int]int)
	x, y := 0, 0
	v[[2]int{0, 0}] = 1
	for _, d := range path {
		if d == 'N' {
			x++
		} else if d == 'S' {
			x--
		} else if d == 'W' {
			y--
		} else {
			y++
		}
		if _, ok := v[[2]int{x, y}]; ok {
			return true
		}
		v[[2]int{x, y}] = 1
	}
	return false
}
