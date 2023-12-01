import "slices"

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	var a []byte
	var b []byte
	for _, w := range word1 {
		a = append(a, []byte(w)...)
	}
	for _, w := range word2 {
		b = append(b, []byte(w)...)
	}
	return slices.Equal(a, b)
}
