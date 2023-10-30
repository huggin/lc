func countBit(n int) int {
    ans := 0
    for n > 0 {
        ans++
        n &= (n-1)
    }
    return ans
}

func sortByBits(arr []int) []int {
    slices.SortFunc(arr, func(a, b int) int {
        ca := countBit(a)
        cb := countBit(b)
        if ca < cb {
            return -1
        } else if ca > cb {
            return 1
        } else if a < b {
            return -1
        } else if a > b {
            return 1
        }
        return 0
    })
    return arr
}
