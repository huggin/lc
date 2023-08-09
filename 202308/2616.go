import "sort"

func minimizeMax(nums []int, p int) int {
	sort.Ints(nums)
	n := len(nums)
	lo, hi := 0, nums[n-1]

	ok := func(v int) bool {
		cnt := 0
		for i := 1; i < n; i++ {
			if nums[i]-nums[i-1] <= v {
				cnt++
				i++
			}
		}
		if cnt >= p {
			return true
		}
		return false
	}

	ans := -1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if ok(mid) {
			ans = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return ans
}
