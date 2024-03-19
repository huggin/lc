class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord("A")] += 1

        cnt.sort()
        tot = sum(cnt)
        same = 1
        for i in range(25):
            if cnt[i] == cnt[25]:
                same += 1

        ans = (cnt[25] - 1) * (n + 1) + same
        m = len(tasks)
        return ans if ans > m else m
