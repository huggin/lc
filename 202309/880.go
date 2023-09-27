func decodeAtIndex(s string, k int) string {
	cnt := int64(0)
	prev := int64(-1)
	K := int64(k - 1)

	var stack [][2]int64
	for i, c := range s {
		if c >= 'a' && c <= 'z' {
			if prev == -1 {
				prev = int64(i)
			}
			cnt++
			if cnt == K+1 {
				return s[i : i+1]
			}
		} else {
			if prev != -1 {
				stack = append(stack, [2]int64{prev, int64(i)})
				prev = -1
			}
			cnt *= int64(c - '0')
			stack = append(stack, [2]int64{-1, int64(c - '0')})
		}
		for len(stack) > 0 && cnt >= K+1 {
			top := stack[len(stack)-1]
			stack = stack[0 : len(stack)-1]
			if top[0] == -1 {
				K %= cnt / top[1]
				cnt /= top[1]
			} else {
				if K+top[1]-top[0] >= cnt {
					idx := int(K + top[1] - cnt)
					return s[idx : idx+1]
				} else {
					cnt -= top[1] - top[0]
				}
			}
		}
	}

	return s
}
