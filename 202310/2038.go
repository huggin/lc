func winnerOfGame(colors string) bool {
	alice := 0
	bob := 0
	n := len(colors)
	for i := 2; i < n; i++ {
		if colors[i] == 'A' && colors[i-1] == 'A' && colors[i-2] == 'A' {
			alice++
		} else if colors[i] == 'B' && colors[i-1] == 'B' && colors[i-2] == 'B' {
			bob++
		}
	}
	return alice > bob
}
