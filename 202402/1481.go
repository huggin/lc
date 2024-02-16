import "sort"

func findLeastNumOfUniqueInts(arr []int, k int) int {
	cnt := make(map[int]int)
	for _, a := range arr {
		cnt[a]++
	}
	sort.Slice(arr, func(i, j int) bool {
		if cnt[arr[i]] < cnt[arr[j]] {
			return true
		}
		return false
	})
	for _, a := range arr {
		if k >= cnt[a] {
			k -= cnt[a]
			cnt[a] = 0
		} else {
			cnt[a] -= k
			break
		}
	}
	ans := 0
	for _, v := range cnt {
		if v != 0 {
			ans++
		}
	}
	return ans
}
