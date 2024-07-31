class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def f(k, w, h):
            if k == n:
                return h
            if w == 0:
                return f(k + 1, books[k][0], books[k][1])
            ans = h + f(k, 0, 0)
            if books[k][0] + w <= shelfWidth:
                ans = min(ans, f(k + 1, books[k][0] + w, max(h, books[k][1])))
            return ans

        return f(0, 0, 0)
