class Solution(object):
    def subarrayBitwiseORs(self, arr):
        n = len(arr)
        dp = set([arr[0]])
        tt = dp.copy()
        for i in range(1, n):
            dp2 = set()
            dp2.add(arr[i])
            for a in dp:
                dp2.add(a | arr[i])
            dp = dp2
            for a in dp:
                tt.add(a)

        return len(tt)
