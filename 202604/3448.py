class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        d = defaultdict(list)
        for i, a in enumerate(nums):
            d[a].append(i)

        m = len(queries)
        ans = [-1] * m
        for i in range(m):
            j = nums[queries[i]]
            if len(d[j]) > 1:
                k = bisect.bisect_left(d[j], queries[i])
                if k == 0:
                    ans[i] = min(d[j][1] - d[j][0], d[j][0] + n - d[j][len(d[j]) - 1])
                elif k == len(d[j]) - 1:
                    ans[i] = min(
                        d[j][len(d[j]) - 1] - d[j][len(d[j]) - 2],
                        d[j][0] + n - d[j][len(d[j]) - 1],
                    )
                else:
                    ans[i] = min(d[j][k] - d[j][k - 1], d[j][k + 1] - d[j][k])
        return ans
