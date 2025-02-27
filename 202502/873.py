class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)

        @cache
        def f(a, b):
            if a + b not in s:
                return 2
            return 1 + f(b, a + b)

        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] in s:
                    ans = max(ans, f(arr[i], arr[j]))
        return ans
