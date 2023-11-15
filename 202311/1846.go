import "slices"

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
	slices.Sort(arr)
	if arr[0] != 1 {
		arr[0] = 1
	}
	n := len(arr)
	for i := 1; i < n; i++ {
		arr[i] = min(arr[i-1]+1, arr[i])
	}
	return arr[n-1]
}
