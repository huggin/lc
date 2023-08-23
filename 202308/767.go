func reorganizeString(s string) string {
    n := len(s)
    cnt := make([]int, 26)
    for _, c := range s {
        cnt[c-'a']++
    }
    ma := 0
    for i:=0; i<26; i++ {
        ma = max(ma, cnt[i])
    }
    if ma > (n + 1) / 2 {
        return ""
    }
    ans := make([]byte, 0)
    for i:=0; i<n; i++ {
        pos, ma := -1, -1
        for j:=0; j<26; j++ {
            if cnt[j] > ma && (len(ans) == 0 || int(ans[len(ans)-1]) - 'a' != j) {
                ma = cnt[j]
                pos = j
            }
        }
        ans = append(ans, byte('a'+pos))
        cnt[pos]--
    }
    return string(ans)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
