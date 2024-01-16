import "math/rand"

type RandomizedSet struct {
	dict map[int]int
	rev  map[int]int
	data []int
}

func Constructor() RandomizedSet {
	var rs RandomizedSet
	rs.dict = make(map[int]int)
	rs.rev = make(map[int]int)
	rs.data = make([]int, 0)
	return rs
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.dict[val]; ok {
		return false
	} else {
		this.data = append(this.data, val)
		idx := len(this.data) - 1
		this.dict[val] = idx
		this.rev[idx] = val
		return true
	}
}

func (this *RandomizedSet) Remove(val int) bool {
	if idx, ok := this.dict[val]; ok {
		last := len(this.data) - 1
		last_val := this.rev[last]
		this.dict[last_val] = idx
		this.rev[idx] = last_val
		this.data[idx], this.data[last] = this.data[last], this.data[idx]
		delete(this.dict, val)
		delete(this.rev, last)
		this.data = this.data[0:last]
		return true
	} else {
		return false
	}
}

func (this *RandomizedSet) GetRandom() int {
	n := len(this.data)
	if n == 0 {
		return 0
	}
	return this.data[rand.Intn(n)]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
