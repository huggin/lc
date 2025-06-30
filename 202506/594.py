class Solution:
    def findLHS(self, nums: List[int]) -> int:
        C = Counter(nums)
        cnt = sorted(C.items())
        ans = 0
        for i in range(1, len(cnt)):
            if cnt[i - 1][0] + 1 == cnt[i][0]:
                ans = max(ans, cnt[i - 1][1] + cnt[i][1])
        return ans
