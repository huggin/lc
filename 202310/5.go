import (
	"bytes"
)

func longestPalindrome(s string) string {
	bs := []byte{'^', '#'}
	n := len(s)
	for i := 0; i < n; i++ {
		bs = append(bs, s[i], '#')
	}
	bs = append(bs, '$')

	p := manacher(bs)
	mi := -1
	ma := 0

	for i := 0; i < len(p); i++ {
		if p[i] > ma {
			ma = p[i]
			mi = i
		}
	}

	ans := bs[mi-p[mi]+3 : mi+p[mi]]
	parts := bytes.Split(ans, []byte("#"))

	return string(bytes.Join(parts, []byte("")))
}

func manacher(s []byte) []int {
	n := len(s)
	p := make([]int, n)
	l := 1
	r := 1
	for i := 1; i <= n-2; i++ {
		p[i] = max(0, min(r-i, p[l+r-i]))
		for s[i-p[i]] == s[i+p[i]] {
			p[i]++
		}
		if i+p[i] > r {
			l = i - p[i]
			r = i + p[i]
		}
	}
	return p[1 : n-2]
}
