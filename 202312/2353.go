import (
	pq "github.com/emirpasic/gods/queues/priorityqueue"
)

type Element struct {
	name   string
	rating int
}

func byPriority(a, b interface{}) int {
	pA := a.(Element)
	pB := b.(Element)
	if pA.rating == pB.rating {
		if pA.name < pB.name {
			return -1
		} else {
			return 1
		}
	}
	return pB.rating - pA.rating
}

type FoodRatings struct {
	f2c  map[string]string
	cs   map[string]*pq.Queue
	rate map[string]int
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	var ans FoodRatings
	ans.f2c = make(map[string]string)
	ans.cs = make(map[string]*pq.Queue)
	ans.rate = make(map[string]int)
	n := len(foods)
	for i := 0; i < n; i++ {
		ans.f2c[foods[i]] = cuisines[i]
		if _, ok := ans.cs[cuisines[i]]; !ok {
			ans.cs[cuisines[i]] = pq.NewWith(byPriority)
		}
		ans.cs[cuisines[i]].Enqueue(Element{foods[i], ratings[i]})
		ans.rate[foods[i]] = ratings[i]
	}
	return ans
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
	cuisine := this.f2c[food]
	this.cs[cuisine].Enqueue(Element{food, newRating})
	this.rate[food] = newRating
}

func (this *FoodRatings) HighestRated(cuisine string) string {
	v, _ := this.cs[cuisine]
	for {
		t, _ := v.Peek()
		top := t.(Element)
		if top.rating != this.rate[top.name] {
			v.Dequeue()
		} else {
			return top.name
		}
	}
	return ""
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * obj := Constructor(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * param_2 := obj.HighestRated(cuisine);
 */
