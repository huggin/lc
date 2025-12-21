class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        ans = 0
        done = [False] * len(strs)
        for i in range(n):
            d2 = done[:]
            removed = False
            for j in range(len(strs) - 1):
                if d2[j] or strs[j][i] < strs[j+1][i]:
                    d2[j] = True
                elif strs[j][i] > strs[j+1][i]:
                    ans += 1
                    removed = True
                    break
            if not removed:
                done = d2
        return ans
