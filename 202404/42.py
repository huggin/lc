class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        if n < 3:
            return 0
        L, R = height[0], height[n - 1]
        l, r = 0, n - 1
        while l < r:
            if L < R:
                l += 1
                ans += max(0, L - height[l])
                L = max(L, height[l])
            else:
                r -= 1
                ans += max(0, R - height[r])
                R = max(R, height[r])

        return ans
