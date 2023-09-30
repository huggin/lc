func find132pattern(nums []int) bool {
	var stack [][2]int
	mi := int(1e9 + 5)
	for _, a := range nums {
		if a < mi {
			mi = a
		} else {
			for len(stack) > 0 {
				top := stack[len(stack)-1]
				if top[0] < a && a < top[1] {
					return true
				}
				if a > top[1] {
					if mi > top[0] {
						mi = top[0]
					}
					stack = stack[0 : len(stack)-1]
				} else {
					break
				}
			}
			stack = append(stack, [2]int{mi, a})
		}

	}
	return false
}
