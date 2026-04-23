class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = defaultdict(list)
        for i in range(n):
            d[nums[i]].append(i)
        
        ans = [0] * n
        for v in d.values():
            pre = [0]
            suf = [0]
            for i in range(len(v)):
                pre.append(pre[-1] + v[i])
            for i in range(len(v) - 1, -1, -1):
                suf.append(suf[-1] + v[i])
            for i in range(len(v)):
                ans[v[i]] = (v[i] * i - pre[i]) + (suf[len(v) - i] - v[i] * (len(v) - i))
        return ans

