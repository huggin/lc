a = [1]
c = [1]
while a[-1] <= 10**9:
    a.append(a[-1] * 4)
    c.append(c[-1] + 1)


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            cnt = 0
            i = bisect.bisect_right(a, l)
            if r >= a[i]:
                cnt += (a[i] - l) * c[i - 1]
            else:
                cnt = (r - l + 1) * c[i - 1]
            for j in range(i + 1, len(a)):
                if a[j - 1] > r:
                    break
                elif r >= a[j]:
                    cnt += (a[j] - a[j - 1]) * c[j - 1]
                else:
                    cnt += (r - a[j - 1] + 1) * c[j - 1]

            ans += (cnt + 1) // 2
        return ans
