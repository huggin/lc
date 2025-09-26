class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0:
            return str(n // d)
        if n == 0:
            return "0"
        ans = []
        if n * d < 0:
            ans.append("-")
            n = abs(n)
            d = abs(d)

        ans.append(str(n // d) + ".")
        n %= d
        xs = []
        r = []

        while True:
            if n in r:
                for i, a in enumerate(r):
                    if a == n:
                        ans.append("(")
                    ans.append(str(xs[i]))
                ans.append(")")
                break
            r.append(n)
            n *= 10
            if n % d == 0:
                xs.append(n // d)
                return "".join(ans) + "".join(str(c) for c in xs)

            c = n // d
            n %= d
            xs.append(c)

        return "".join(ans)
