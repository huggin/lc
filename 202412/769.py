class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        v = [0] * n
        ans = 0
        ma = -1
        for i in range(n):
            flag = True
            v[arr[i]] = 1
            ma = max(ma, arr[i])
            for j in range(0, ma):
                if v[j] == 0:
                    flag = False
                    break
            if flag:
                ans += 1
                ma = -1
        return ans
