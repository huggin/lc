func rangeBitwiseAnd(left int, right int) int {
	ans := 0
	for i := 0; i < 32; i++ {
		if right == left {
			ans |= (left << i)
		}
		right >>= 1
		left >>= 1
	}
	return ans
}
