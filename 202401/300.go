import "sort"

func lengthOfLIS(nums []int) int {
	var lis []int
	for _, a := range nums {
		i := sort.SearchInts(lis, a)
		if i == len(lis) {
			lis = append(lis, a)
		} else {
			lis[i] = a
		}
	}
	return len(lis)
}
