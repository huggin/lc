class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s
        for i in range(len(chalk)):
            if k >= chalk[i]:
                k -= chalk[i]
            else:
                return i
        return -1
