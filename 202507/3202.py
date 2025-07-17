class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        a = [c % k for c in nums]
        ans = Counter(a).most_common(1)[0][1]

        n = len(a)
        s = set()
        for i in range(n):
            if a[i] in s:
                continue
            s.add(a[i])
            cnt = [1] * k
            s2 = set()
            for kk in range(i + 1, n):
                if a[kk] != a[i]:
                    if a[kk] not in s2:
                        s2.add(a[kk])
                        cnt[a[kk]] += 1
                        kk += 1
                else:
                    for c in s2:
                        cnt[c] += 1
                    s2 = set()

            for j in range(k):
                ans = max(ans, cnt[j])

        return ans
