class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        ans = []
        n = len(code)
        for i in range(n):
            if not isActive[i]:
                continue
            if businessLine[i] not in set(
                ["electronics", "grocery", "pharmacy", "restaurant"]
            ):
                continue
            flag = True
            for j in range(len(code[i])):
                if not (code[i][j].isalnum() or code[i][j] == "_"):
                    flag = False
                    break
            if flag and len(code[i]) > 0:
                ans.append([code[i], businessLine[i]])

        ans.sort(key=lambda x: (x[1], x[0]))
        return list(c[0] for c in ans)
