class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        a = []
        n = len(profit)
        for i in range(n):
            a.append((profit[i], difficulty[i]))

        a.sort(key=lambda x: (-x[0], x[1]))
        worker.sort(reverse=True)
        print(a, worker)
        i, j = 0, 0
        ans = 0
        while i < n and j < len(worker):
            if a[i][1] <= worker[j]:
                ans += a[i][0]
                j += 1
            else:
                i += 1
        return ans
