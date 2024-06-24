class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        n = len(nums)
        ans = 0
        for i in range(n):
            if len(q) > 0 and q[0] == i - k:
                q.popleft()
            if (nums[i] + len(q)) % 2 == 0:
                if n - i < k:
                    return -1
                ans += 1
                q.append(i)

        return ans
