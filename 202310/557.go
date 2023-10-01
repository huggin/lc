import "strings"

func reverseWords(s string) string {
	words := strings.Split(s, " ")
	for i := 0; i < len(words); i++ {
		words[i] = reverse(words[i])
	}
	return strings.Join(words, " ")
}

func reverse(s string) string {
	n := len(s)
	bytes := make([]byte, n)
	for i := 0; i < n; i++ {
		bytes[i] = s[n-1-i]
	}
	return string(bytes)
}
