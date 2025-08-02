class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)
        for k, v in cnt1.items():
            if k in cnt2:
                if v <= cnt2[k]:
                    cnt1[k] = 0
                    cnt2[k] -= v
                else:
                    cnt1[k] -= cnt2[k]
                    cnt2[k] = 0

        a = []
        for k, v in cnt1.items():
            if v == 0:
                continue
            if v % 2 == 1:
                return -1
            for i in range(v // 2):
                a.append(k)

        for k, v in cnt2.items():
            if v == 0:
                continue
            if v % 2 == 1:
                return -1
            for i in range(v // 2):
                a.append(k)

        a.sort()
        n = len(a)

        mi = min(min(basket1), min(basket2))
        ans = 0
        for i in range(n // 2):
            ans += min(mi * 2, a[i])
        return ans
