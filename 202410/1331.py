class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sa = sorted(arr)
        n = len(arr)
        if n == 0:
            return []
        rank = {}
        rank[sa[0]] = 1
        for i in range(1, n):
            if sa[i] == sa[i - 1]:
                rank[sa[i]] = rank[sa[i - 1]]
            else:
                rank[sa[i]] = rank[sa[i - 1]] + 1

        ans = [0] * n
        for i in range(n):
            ans[i] = rank[arr[i]]
        return ans
