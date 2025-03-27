class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        a, m = Counter(nums).most_common()[0]
        cnt = 0
        for i in range(n):
            if nums[i] == a:
                cnt += 1
            if cnt + cnt > i + 1 and (m - cnt) * 2 > n - (i+1):
                return i
        return -1
