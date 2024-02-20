func missingNumber(nums []int) int {
	var cnt [16]int
	for i := 1; i < len(nums)+1; i++ {
		for j := 0; j < 16; j++ {
			if (i & (1 << j)) != 0 {
				cnt[j]++
			}
		}
	}
	for _, a := range nums {
		for i := 0; i < 16; i++ {
			if (a & (1 << i)) != 0 {
				cnt[i]--
			}
		}
	}
	ans := 0
	for i := 0; i < 16; i++ {
		if cnt[i] == 1 {
			ans |= (1 << i)
		}
	}
	return ans
}
