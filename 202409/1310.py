class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] ^ arr[i]

        return list(ps[r + 1] ^ ps[l] for l, r in queries)
