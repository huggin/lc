import "slices"

func sortVowels(s string) string {
	v := map[byte]bool{
		'a': true, 'e': true, 'i': true, 'o': true, 'u': true,
		'A': true, 'E': true, 'I': true, 'O': true, 'U': true,
	}

	var vowels []byte
	n := len(s)
	for i := 0; i < n; i++ {
		if v[s[i]] {
			vowels = append(vowels, s[i])
		}
	}
	slices.Sort(vowels)

	ans := make([]byte, n)
	j := 0
	for i := 0; i < n; i++ {
		if v[s[i]] {
			ans[i] = vowels[j]
			j++
		} else {
			ans[i] = s[i]
		}
	}
	return string(ans)
}
