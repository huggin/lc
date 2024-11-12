class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(queries)
        ans = [0] * n

        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        for i in range(n):
            j = bisect.bisect(items, [queries[i] + 1, 0])
            ans[i] = items[j - 1][1] if j > 0 else 0

        return ans
