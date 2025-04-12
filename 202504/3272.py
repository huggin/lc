class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        m = (n + 1) // 2
        curr = []
        s = set()

        def value(a):
            ans = 0
            for c in a:
                ans = ans * 10 + c
            return ans

        def dfs(j):
            if j == m:
                if m * 2 == n:
                    a = value(curr + curr[::-1])
                    if a % k == 0:
                        s.add(tuple(sorted(curr + curr[::-1])))
                else:
                    a = value(curr + curr[-2::-1])
                    if a % k == 0:
                        s.add(tuple(sorted(curr + curr[-2::-1])))
                return
            if j == 0:
                for i in range(1, 10):
                    curr.append(i)
                    dfs(j + 1)
                    curr.pop()
            else:
                for i in range(10):
                    curr.append(i)
                    dfs(j + 1)
                    curr.pop()

        dfs(0)
        ans = 0

        fact = [1] * 11
        for i in range(1, 11):
            fact[i] = fact[i - 1] * i

        for a in s:
            c = Counter(a)
            if c[0] == 0:
                temp = fact[n]
                for i in range(1, 10):
                    if c[i] != 0:
                        temp //= fact[c[i]]
            else:
                temp = fact[n - 1] // fact[c[0]] // fact[n - 1 - c[0]] * fact[n - c[0]]
                for i in range(1, 10):
                    if c[i] != 0:
                        temp //= fact[c[i]]
            ans += temp
        return ans
