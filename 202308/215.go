func partition(nums []int, lo, hi int) int {
	pivot := nums[lo]
	j := lo
	for i := lo + 1; i <= hi; i++ {
		if nums[i] > pivot {
			j++
			nums[j], nums[i] = nums[i], nums[j]
		}
	}
	nums[j], nums[lo] = nums[lo], nums[j]
	return j
}

func findKth(nums []int, lo, hi int, k int) int {
	pivot := partition(nums, lo, hi)
	if pivot-lo+1 == k {
		return nums[pivot]
	} else if pivot-lo+1 < k {
		return findKth(nums, pivot+1, hi, k-(pivot-lo+1))
	} else {
		return findKth(nums, lo, pivot-1, k)
	}
}

func findKthLargest(nums []int, k int) int {
	n := len(nums)
	return findKth(nums, 0, n-1, k)
}
