func destCity(paths [][]string) string {
	degree := make(map[string]int)
	for _, p := range paths {
		degree[p[1]]++
		degree[p[0]]--
	}
	for k, v := range degree {
		if v == 1 {
			return k
		}
	}
	return "Leetcode"
}
