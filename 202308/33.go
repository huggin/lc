func search(nums []int, target int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if target == nums[mid] {
			return mid
		} else if target == nums[lo] {
			return lo
		} else if target == nums[hi] {
			return hi
		} else {
			if nums[lo] < nums[mid] {
				if nums[lo] < target && target < nums[mid] {
					hi = mid - 1
				} else {
					lo = mid + 1
				}
			} else {
				if nums[mid] < target && target < nums[hi] {
					lo = mid + 1
				} else {
					hi = mid - 1
				}
			}
		}
	}
	return -1
}
