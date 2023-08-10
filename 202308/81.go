func search2(nums []int, lo, hi int, target int) bool {
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if target == nums[lo] || target == nums[hi] || target == nums[mid] {
			return true
		}
		if nums[lo] < nums[mid] {
			if target > nums[lo] && target < nums[mid] {
				hi = mid - 1
			} else {
				return search2(nums, lo+1, mid-1, target) || search2(nums, mid+1, hi-1, target)
			}
		} else if nums[mid] < nums[hi] {
			if target > nums[mid] && target < nums[hi] {
				lo = mid + 1
			} else {
				return search2(nums, lo+1, mid-1, target) || search2(nums, mid+1, hi-1, target)
			}
		} else {
			return search2(nums, lo+1, mid-1, target) || search2(nums, mid+1, hi-1, target)
		}
	}
	return false
}

func search(nums []int, target int) bool {
	lo, hi := 0, len(nums)-1
	return search2(nums, lo, hi, target)
}
