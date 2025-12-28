class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 51
        n = len(nums)
        for i in range(k):
            cnt[nums[i]] += 1

        ans = [0] * (n - k + 1)

        def f():
            s = set()
            ans = 0
            while len(s) < x:
                k = -1
                c = 1
                for j in range(51):
                    if j not in s and cnt[j] >= c:
                        k = j
                        c = cnt[j]
                if k == -1:
                    break
                s.add(k)
                ans += k * c
            return ans

        ans[0] = f()
        for i in range(k, n):
            cnt[nums[i - k]] -= 1
            cnt[nums[i]] += 1
            ans[i - k + 1] = f()

        return ans
