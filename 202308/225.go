type MyStack struct {
	q1 []int
	q2 []int
}

func Constructor() MyStack {
	var stack MyStack
	return stack
}

func (this *MyStack) Push(x int) {
	if len(this.q2) > 0 {
		this.q2 = append(this.q2, x)
	} else {
		this.q1 = append(this.q1, x)
	}
}

func (this *MyStack) Pop() int {
	var ans int
	if len(this.q1) > 0 {
		for len(this.q1) > 1 {
			this.q2 = append(this.q2, this.q1[0])
			this.q1 = this.q1[1:]
		}
		ans = this.q1[0]
		this.q1 = nil
	} else {
		for len(this.q2) > 1 {
			this.q1 = append(this.q1, this.q2[0])
			this.q2 = this.q2[1:]
		}
		ans = this.q2[0]
		this.q2 = nil
	}
	return ans
}

func (this *MyStack) Top() int {
	var ans int
	if len(this.q1) > 0 {
		for len(this.q1) > 1 {
			this.q2 = append(this.q2, this.q1[0])
			this.q1 = this.q1[1:]
		}
		ans = this.q1[0]
		this.q1 = nil
		this.q2 = append(this.q2, ans)
	} else {
		for len(this.q2) > 1 {
			this.q1 = append(this.q1, this.q2[0])
			this.q2 = this.q2[1:]
		}
		ans = this.q2[0]
		this.q2 = nil
		this.q1 = append(this.q1, ans)
	}
	return ans
}

func (this *MyStack) Empty() bool {
	return len(this.q1) == 0 && len(this.q2) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
