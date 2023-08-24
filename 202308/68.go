func fullJustify(words []string, maxWidth int) []string {
	var ans []string
	n := 0
	j := 0

	for i, w := range words {
		if n+len(w) > maxWidth {
			s := construct(j, i-1, words, maxWidth, false)
			ans = append(ans, s)
			n = len(w)
			j = i
			n++
		} else {
			n += 1 + len(w)
		}

	}
	s := construct(j, len(words)-1, words, maxWidth, true)
	ans = append(ans, s)
	return ans
}

func construct(j, i int, words []string, wd int, last bool) string {
	buf := make([]byte, wd)
	idx := 0
	n := 0
	for k := j; k <= i; k++ {
		n += len(words[k])
	}
	spaces := wd - n
	av := spaces
	more := 0
	if i != j {
		av = spaces / (i - j)
		more = spaces % (i - j)
	}
	if last {
		av = 1
		more = 0
	}
	for k := j; k <= i; k++ {
		for l := 0; l < len(words[k]); l, idx = l+1, idx+1 {
			buf[idx] = words[k][l]
		}
		if k != i {
			sp := av
			if more > 0 {
				sp++
				more--
			}
			for sp > 0 {
				buf[idx] = ' '
				idx++
				sp--
			}
		}
	}
	for idx < wd {
		buf[idx] = ' '
		idx++
	}
	return string(buf)
}
