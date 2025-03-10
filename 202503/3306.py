class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        unique = 0
        cnt = [0] * 6
        d = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        a = [d.get(c, 5) for c in word]
        l, r = 0, 0
        n = len(a)
        ans = 0
        for i in range(n):
            while l < n and (unique < 5 or cnt[5] < k):
                cnt[a[l]] += 1
                if a[l] < 5:
                    if cnt[a[l]] == 1:
                        unique += 1
                l += 1
            if unique == 5 and cnt[5] == k:
                r = max(r, l - 1)
                while r + 1 < n and a[r+1] < 5:
                    r += 1
                ans += r - l + 2
            cnt[a[i]] -= 1
            if a[i] < 5:
                if cnt[a[i]] == 0:
                    unique -= 1
            
        return ans
