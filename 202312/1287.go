func findSpecialInteger(arr []int) int {
	freq := make(map[int]int)
	for _, a := range arr {
		freq[a]++
	}
	ans := -1
	max := -1
	for k, v := range freq {
		if v > max {
			max = v
			ans = k
		}
	}
	return ans
}  
