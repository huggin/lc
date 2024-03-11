import "sort"

func customSortString(order string, s string) string {
	o := make(map[byte]int)
	for i := 0; i < len(order); i++ {
		o[order[i]] = i
	}
	b := []byte(s)
	sort.Slice(b, func(i, j int) bool {
		if o[b[i]] < o[b[j]] {
			return true
		}
		return false
	})
	return string(b)
}
