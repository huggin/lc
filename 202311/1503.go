func getLastMoment(n int, left []int, right []int) int {
    ans := 0
    for _, a := range left {
        ans = max(ans, a)
    }
    for _, a := range right {
        ans = max(ans, n - a)
    }
    return ans
}
