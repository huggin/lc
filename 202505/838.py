class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        a = [c for c in dominoes]
        n = len(a)
        prev = " "
        j = -1
        for i in range(n):
            if a[i] != ".":
                j = i
                prev = a[j]
                break
        if j == -1:
            return dominoes
        if a[j] == "L":
            for k in range(j):
                a[k] = "L"
        while True:
            i = j + 1
            while i < n and a[i] == ".":
                i += 1
            if i == n:
                if prev == "R":
                    for k in range(j + 1, n):
                        a[k] = "R"
                break

            if prev == "R" and a[i] == "L":
                j1 = j + 1
                i1 = i - 1
                while j1 < i1:
                    a[j1] = "R"
                    a[i1] = "L"
                    j1, i1 = j1 + 1, i1 - 1
                prev = "L"
            elif prev == a[i]:
                for k in range(j + 1, i):
                    a[k] = prev
            else:
                prev = "R"
            j = i

        return "".join(a)
