class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa, sb = set(), set()
        n = len(A)
        ans = [0] * (n + 1)
        for i in range(n):
            ans[i + 1] = ans[i]
            if A[i] in sb:
                ans[i + 1] += 1
            if B[i] in sa:
                ans[i + 1] += 1
            if A[i] == B[i]:
                ans[i + 1] += 1
            sa.add(A[i])
            sb.add(B[i])

        return ans[1:]
