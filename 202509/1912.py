class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = {}
        self.shops = {}
        self.rented = SortedList()
        for shop, movie, price in entries:
            if movie not in self.movies:
                self.movies[movie] = SortedList()
            self.movies[movie].add((price, shop))
            if shop not in self.shops:
                self.shops[shop] = {}
            self.shops[shop][movie] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies:
            return []
        return list(shop for _, shop in self.movies[movie][0:5])

    def rent(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.movies[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.rented.remove((price, shop, movie))
        self.movies[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return list([shop, movie] for _, shop, movie in self.rented[0:5])


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
