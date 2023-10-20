/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

type NestedIterator struct {
	li   []*NestedInteger
	i    int
	curr []int
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	var itor NestedIterator
	itor.li = nestedList
	itor.i = 0
	return &itor
}

func (this *NestedIterator) fill(list []*NestedInteger) {
	for _, v := range list {
		if v.IsInteger() {
			this.curr = append(this.curr, v.GetInteger())
		} else {
			this.fill(v.GetList())
		}
	}
}

func (this *NestedIterator) Next() int {
	if len(this.curr) > 0 {
		ans := this.curr[0]
		this.curr = this.curr[1:]
		return ans
	}
	return 0
}

func (this *NestedIterator) HasNext() bool {
	if len(this.curr) > 0 {
		return true
	}
	for len(this.curr) == 0 && this.i < len(this.li) {
		if this.li[this.i].IsInteger() {
			this.curr = append(this.curr, this.li[this.i].GetInteger())
		} else {
			this.fill(this.li[this.i].GetList())
		}
		this.i++
	}
	if len(this.curr) > 0 {
		return true
	}
	return false
}
