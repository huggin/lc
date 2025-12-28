class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        ans = [0] * value
        for a in nums:
            ans[a % value] += 1
        cnt = min(ans)
        for i in range(value):
            if ans[i] == cnt:
                return i + value * ans[i]
        return -1
