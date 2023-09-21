import "math"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m := len(nums1)
	n := len(nums2)
	if m > n {
		return findMedianSortedArrays(nums2, nums1)
	}

	l, r := 0, len(nums1)
	for l <= r {
		i := l + (r-l)/2
		j := (m+n+1)/2 - i
		var aleft, aright, bleft, bright int
		if i < len(nums1) {
			aright = nums1[i]
		} else {
			aright = math.MaxInt32
		}
		if i > 0 {
			aleft = nums1[i-1]
		} else {
			aleft = math.MinInt32
		}
		if j > 0 && j-1 < len(nums2) {
			bleft = nums2[j-1]
		} else {
			bleft = math.MinInt32
		}
		if j >= 0 && j < len(nums2) {
			bright = nums2[j]
		} else {
			bright = math.MaxInt32
		}

		if aleft <= bright && bleft <= aright {
			if (n+m)%2 == 1 {
				return float64(max(aleft, bleft))
			} else {
				return float64(max(aleft, bleft)+min(aright, bright)) / 2
			}
		} else if aleft > bright {
			r = i - 1
		} else {
			l = i + 1
		}
	}
	return 0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
