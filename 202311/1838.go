import "slices"

func maxFrequency(nums []int, k int) int {
	slices.Sort(nums)
	n := len(nums)
	presum := make([]int, n+1)
	presum[0] = 0
	for i := 0; i < n; i++ {
		presum[i+1] = presum[i] + nums[i]
	}
	ans := 1
	j := 0
	for i := 0; i < n; i++ {
		for (presum[i+1]-presum[j]+k)/(i+1-j) < nums[i] {
			j++
		}
		ans = max(ans, i+1-j)
	}
	return ans
}
