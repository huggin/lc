class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        cnt = [[0 for _ in range(n+1)] for _ in range(26)]
        p = ' '
        curr = 0
        for c in s:
            if c != p:
                if curr != 0:
                    cnt[ord(p) - ord('a')][curr] += 1
                curr = 1
            else:
                curr += 1
            p = c
        
        cnt[ord(p) - ord('a')][curr] += 1
        ans = -1
        for i in range(26):
            k = -1
            for j in range(n, 0, -1):
                if cnt[i][j] != 0:
                    k = j
                    break
            if k != -1:
                if cnt[i][k] >= 3:
                    ans = max(ans, k)
                elif (cnt[i][k] >= 2 or cnt[i][k] == 1 and cnt[i][k-1] >= 1) and k - 1 > 0:
                    ans = max(ans, k-1)
                elif cnt[i][k] == 1 and k >= 3:
                    ans = max(ans, k-2)
        return ans
