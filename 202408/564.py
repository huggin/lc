class Solution:
    def getSmall(self, s) -> list:
        n = len(s)
        i = (n - 1) // 2
        j = i
        while i >= 0 and s[i] == "0":
            i -= 1
        if i < 0 or i == 0 and s[i] == "1":
            return "9" * (n - 1)
        ans = [c for c in s]
        ans[i] = str(int(s[i]) - 1)
        ans[n - 1 - i] = ans[i]
        while j > i:
            ans[j] = "9"
            ans[n - 1 - j] = "9"
            j -= 1

        return "".join(ans)

    def getBig(self, s) -> list:
        n = len(s)
        i = (n - 1) // 2
        j = i
        while i >= 0 and s[i] == "9":
            i -= 1
        if i < 0:
            return "1" + "0" * (n - 1) + "1"
        ans = [c for c in s]
        ans[i] = str(int(s[i]) + 1)
        ans[n - 1 - i] = ans[i]
        while j > i:
            ans[j] = "0"
            ans[n - 1 - j] = "0"
            j -= 1
        return "".join(ans)

    def nearestPalindromic(self, n: str) -> str:
        d = int(n)
        if d <= 10:
            return str(d - 1)
        s = n
        m = len(s)
        if m % 2 == 0:
            s = s[0 : m // 2] + s[m // 2 - 1 :: -1]
        else:
            s = s[0 : m // 2 + 1] + s[m // 2 - 1 :: -1]

        small, big = None, None
        if s < n:
            small = s
        elif s > n:
            big = s

        if small is None:
            small = self.getSmall(s)
        if big is None:
            big = self.getBig(s)

        if d - int(small) <= int(big) - d:
            return small

        return big
