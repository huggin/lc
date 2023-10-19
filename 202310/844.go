func getBytes(s string) []byte {
	var s1 []byte
	for _, c := range s {
		if c == '#' {
			if len(s1) > 0 {
				s1 = s1[0 : len(s1)-1]
			}
		} else {
			s1 = append(s1, byte(c))
		}
	}
	return s1
}

func backspaceCompare(s string, t string) bool {
	s1 := getBytes(s)
	t1 := getBytes(t)
	if len(s1) != len(t1) {
		return false
	}
	for i := 0; i < len(s1); i++ {
		if s1[i] != t1[i] {
			return false
		}
	}
	return true
}
