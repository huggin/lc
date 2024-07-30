class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = left[i-1]
            if s[i-1] == 'b':
                left[i] += 1
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]
            if s[i+1] == 'a':
                right[i] += 1
        
        ans = min(left[n-1], right[0])
        for i in range(1, n-1):
            ans = min(ans, left[i] + right[i])
        return ans

