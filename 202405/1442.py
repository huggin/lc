class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ arr[i]

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if pre[j + 1] ^ pre[i] == 0:
                    ans += j - i
        return ans
