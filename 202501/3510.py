class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        pq = []
        a = SortedList()
        for k, v in enumerate(nums):
            a.add((k, v))
        n = len(nums)
        cnt = [0] * n
        for i in range(n - 1):
            heapq.heappush(pq, (nums[i] + nums[i + 1], i))
            cnt[i] = nums[i] + nums[i + 1]

        removed = set()

        ans = 0
        while len(pq) > 0:
            # print(a, pq, cnt)
            v, i = heapq.heappop(pq)
            while len(pq) > 0 and (v, i) == pq[0]:
                heapq.heappop(pq)
            if i in removed:
                continue
            if v != cnt[i]:
                continue
            j = a.bisect((i - 1, float("inf")))
            # print("j=", j)

            if j == 0:
                flag = True
                for k in range(len(a) - 1):
                    if a[k][1] > a[k + 1][1]:
                        flag = False
                        break
                if flag:
                    break
            ans += 1
            if j + 1 < len(a):
                removed.add(a[j + 1][0])
                a.pop(j + 1)
            a.pop(j)
            a.add((i, v))
            if j + 1 < len(a):
                cnt[i] = v + a[j + 1][1]
                heapq.heappush(pq, (v + a[j + 1][1], i))
            if j - 1 >= 0:
                t = v + a[j - 1][1]
                cnt[a[j - 1][0]] = t
                heapq.heappush(pq, (t, a[j - 1][0]))

        return ans
