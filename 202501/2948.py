class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        group = [-1] * n
        a = list((v, k) for k, v in enumerate(nums))
        a.sort()
        groups = []
        cg = []
        value = []
        for i in range(n):
            if len(cg) > 0 and a[i - 1][0] + limit < a[i][0]:
                for j in cg:
                    group[j] = len(groups)
                groups.append(sorted(value))
                cg = []
                value = []
            cg.append(a[i][1])
            value.append(a[i][0])
        for j in cg:
            group[j] = len(groups)
        groups.append(sorted(value))
        idx = [0] * len(groups)

        ans = [0] * n
        for i in range(n):
            ans[i] = groups[group[i]][idx[group[i]]]
            idx[group[i]] += 1

        return ans
