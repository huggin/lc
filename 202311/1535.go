func getWinner(arr []int, k int) int {
    n := len(arr)
    cnt := 1
    ma := arr[0]
    if arr[0] < arr[1] {
        ma = arr[1]
    }
    if cnt == k {
        return ma
    }
    for i:=2; i < n; i++ {
        if arr[i] < ma {
            cnt++
        } else {
            ma = arr[i]
            cnt = 1
        }
        if cnt == k {
            return ma
        }
    }
    return ma
}
