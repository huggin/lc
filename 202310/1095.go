/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 *
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */

func findInMountainArray(target int, mountainArr *MountainArray) int {
	n := mountainArr.length()
	lo, hi := 0, n-1
	idx := -1
	for lo <= hi {
		mid1 := lo + (hi-lo)/3
		mid2 := hi - (hi-lo)/3
		k1 := mountainArr.get(mid1)
		k2 := mountainArr.get(mid2)
		if k1 < k2 {
			idx = mid2
			lo = mid1 + 1
		} else if k1 > k2 {
			idx = mid1
			hi = mid2 - 1
		} else {
			idx = mid1
			lo = mid1 + 1
			hi = mid2 - 1
		}
	}

	lo, hi = 0, idx
	for lo <= hi {
		mid := lo + (hi-lo)/2
		k := mountainArr.get(mid)
		if k == target {
			return mid
		} else if k < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	lo, hi = idx, n-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		k := mountainArr.get(mid)
		if k == target {
			return mid
		} else if k < target {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return -1
}
