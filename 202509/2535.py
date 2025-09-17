class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rate = {}
        self.cate = {}
        self.flavour = {}
        for i, f in enumerate(foods):
            self.rate[f] = ratings[i]
            self.cate[f] = cuisines[i]
            if cuisines[i] not in self.flavour:
                self.flavour[cuisines[i]] = SortedList()
            self.flavour[cuisines[i]].add((-ratings[i], f))

    def changeRating(self, food: str, newRating: int) -> None:
        old = self.rate[food]
        cuisine = self.cate[food]
        self.flavour[cuisine].remove((-old, food))
        self.rate[food] = newRating
        self.flavour[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.flavour[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
