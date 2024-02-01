func divideArray(nums []int, k int) [][]int {
    slices.Sort(nums)
    var ans [][]int
    n := len(nums)
    for i:=0; i < n; i+=3 {
        if nums[i+2] - nums[i] > k {
            return nil
        }
        ans = append(ans, nums[i:i+3])
    }
    return ans
}
