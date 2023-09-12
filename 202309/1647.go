import "sort"

func minDeletions(s string) int {
	var f [26]int
	for i := range s {
		f[s[i]-'a']++
	}
	var f2 []int
	for i := 0; i < 26; i++ {
		if f[i] != 0 {
			f2 = append(f2, f[i])
		}
	}
	sort.Slice(f2, func(i, j int) bool {
		return f2[i] >= f2[j]
	})

	ans := 0
	for i := 1; i < len(f2); i++ {
		if f2[i-1] <= 1 {
			ans += f2[i]
			f2[i] = 0
		} else if f2[i] >= f2[i-1] {
			ans += f2[i] - f2[i-1] + 1
			f2[i] = f2[i-1] - 1
		}
	}
	return ans
}
