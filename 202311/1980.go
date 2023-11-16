func findDifferentBinaryString(nums []string) string {
    n := len(nums)
    var s []byte

    as := make(map[string]bool)
    for _, item := range nums {
        as[item] = true
    }

    var ans string

    var f func(k int)
    f = func(k int) {
        if len(ans) > 0 {
            return
        }
        if k == n {
            if _, ok := as[string(s)]; !ok {
                ans = string(s)
            }
            return
        }
        s = append(s, '0')
        f(k+1)
        s = s[0:len(s)-1]
        s = append(s, '1')
        f(k+1)a
        s = s[0:len(s)-1]
    }
    f(0)
    return ans
}
