class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()
        n = len(tasks)
        m = len(workers)

        def ok(k, p):
            t = tasks[0:k]
            w = SortedList(workers[-k:])
            for i in range(k - 1, -1, -1):
                if w[i] >= t[i]:
                    continue
                else:
                    if p <= 0:
                        return False
                    p -= 1
                    idx = w.bisect_left(t[i] - strength)
                    if idx == i + 1:
                        return False
                    w.pop(idx)

            return True

        ans = 0
        lo, hi = 0, min(n, m)
        while lo <= hi:
            mi = lo + hi >> 1
            if ok(mi, min(pills, mi)):
                ans = mi
                lo = mi + 1
            else:
                hi = mi - 1

        return ans
