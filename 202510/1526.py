class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = 0
        curr = 0
        for i in range(n):
            if target[i] > curr:
                ans += target[i] - curr
            curr = target[i]
        return ans
