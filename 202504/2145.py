class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a = [0]
        for d in differences:
            a.append(a[-1] + d)

        mi = min(a)
        ma = max(a)
        diff = lower - mi
        for i in range(len(a)):
            a[i] += diff
        ma2 = max(a)
        if ma2 > upper:
            return 0

        return upper - ma2 + 1
