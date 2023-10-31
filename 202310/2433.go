func findArray(pref []int) []int {
    n := len(pref)
    ans := make([]int, n)
    ans[0] = pref[0]
    for i:=n-1; i > 0; i-- {
        ans[i] = pref[i-1] ^ pref[i]
    }
    return ans
}
