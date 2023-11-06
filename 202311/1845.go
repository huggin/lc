type SeatManager struct {
	seat []int
	size int
}

func Constructor(n int) SeatManager {
	var sm SeatManager
	sm.size = n
	sm.seat = make([]int, n)
	return sm
}

func (this *SeatManager) Reserve() int {
	for i := 0; i < this.size; i++ {
		if this.seat[i] == 0 {
			this.seat[i] = 1
			return i + 1
		}
	}
	return -1
}

func (this *SeatManager) Unreserve(seatNumber int) {
	this.seat[seatNumber-1] = 0
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
