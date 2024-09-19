class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        @cache
        def f(i, j):
            s = []
            for k in range(i, j + 1):
                if exp[k] == "+" or exp[k] == "-" or exp[k] == "*":
                    s1 = f(i, k - 1)
                    s2 = f(k + 1, j)
                    for a in s1:
                        for b in s2:
                            if exp[k] == "+":
                                s.append(a + b)
                            elif exp[k] == "-":
                                s.append(a - b)
                            else:
                                s.append(a * b)
            if len(s) == 0:
                s.append(int(exp[i : j + 1]))
            return s

        return f(0, len(exp) - 1)
