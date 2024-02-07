func frequencySort(s string) string {
	var cnt [128]int
	for _, c := range s {
		cnt[c]++
	}
	n := len(s)
	b := make([]byte, 0, n)
	for len(b) < n {
		j := byte(255)
		mj := 0
		for i := 0; i < 128; i++ {
			if cnt[i] > mj {
				j = byte(i)
				mj = cnt[i]
			}
		}
		for k := 0; k < mj; k++ {
			b = append(b, j)
		}
		cnt[int(j)] = 0
	}
	return string(b)
}
