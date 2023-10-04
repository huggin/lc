type Node struct {
	Key   int
	Value int
	Next  *Node
}

type MyHashMap struct {
	HashMap [5987]*Node
}

func Constructor() MyHashMap {
	var hm MyHashMap
	return hm
}

func (this *MyHashMap) Put(key int, value int) {
	idx := key % 5987
	p := this.HashMap[idx]
	for p != nil {
		if p.Key == key {
			p.Value = value
			return
		}
		p = p.Next
	}
	node := &Node{key, value, nil}
	node.Next = this.HashMap[idx]
	this.HashMap[idx] = node
}

func (this *MyHashMap) Get(key int) int {
	idx := key % 5987
	p := this.HashMap[idx]
	for p != nil {
		if p.Key == key {
			return p.Value
		}
		p = p.Next
	}
	return -1
}

func (this *MyHashMap) Remove(key int) {
	idx := key % 5987
	p := this.HashMap[idx]
	var prev *Node
	for p != nil {
		if p.Key == key {
			if prev != nil {
				prev.Next = p.Next
			} else {
				this.HashMap[idx] = this.HashMap[idx].Next
			}
			return
		}
		prev = p
		p = p.Next
	}
}
