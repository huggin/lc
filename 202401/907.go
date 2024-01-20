func sumSubarrayMins(arr []int) int {
	n := len(arr)
	left := make([]int, n)
	right := make([]int, n)
	stack := make([]int, 0)
	for i := 0; i < n; i++ {
		for len(stack) > 0 && arr[stack[len(stack)-1]] >= arr[i] {
			stack = stack[0 : len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = 0
		} else {
			left[i] = stack[len(stack)-1] + 1
		}
		stack = append(stack, i)
	}
	stack = make([]int, 0)
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && arr[stack[len(stack)-1]] > arr[i] {
			stack = stack[0 : len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n - 1
		} else {
			right[i] = stack[len(stack)-1] - 1
		}
		stack = append(stack, i)
	}

	ans := 0
	const M = int(1e9 + 7)
	for i := 0; i < n; i++ {
		ans = (ans + arr[i]*(i-left[i]+1)*(right[i]-i+1)%M) % M
	}

	return ans
}
