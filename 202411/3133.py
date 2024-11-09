class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        b = bin(n)
        s = list(str(b)[2:][::-1])

        a = list(str(bin(x))[2:][::-1])
        m = len(a)
        j = 0
        for i in range(len(s)):
            found = False
            while j < m:
                if a[j] == "1":
                    j += 1
                else:
                    a[j] = s[i]
                    j += 1
                    found = True
                    break

            if not found:
                a.append(s[i])

        return int("".join(reversed(a)), 2)
