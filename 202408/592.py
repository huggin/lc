class Solution:
    def fractionAddition(self, e: str) -> str:
        n = len(e)
        a = []
        last = 0
        for i in range(1, n):
            if e[i] == "+" or e[i] == "-":
                a.append(e[last:i])
                a.append(e[i])
                last = i + 1

        a.append(e[last:])
        d1, n1 = map(int, a[0].split("/"))
        for i in range(2, len(a), 2):
            d2, n2 = map(int, a[i].split("/"))
            n3 = math.lcm(n1, n2)
            if a[i - 1] == "+":
                d3 = n3 // n1 * d1 + n3 // n2 * d2
            else:
                d3 = n3 // n1 * d1 - n3 // n2 * d2
            (
                d1,
                n1,
            ) = (
                d3,
                n3,
            )

        g = math.gcd(d1, n1)
        return f"{d1//g}/{n1//g}"
