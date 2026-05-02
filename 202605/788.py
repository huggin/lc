class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        n = len(s)

        @cache
        def f(i, same, small):
            if i == n:
                if same:
                    return 0
                else:
                    return 1
            up = 10 if small else int(s[i]) + 1
            ans = 0
            for j in range(up):
                if j in [0, 1, 8]:
                    ans += f(i+1, same, small or j < int(s[i]))
                elif j in [2, 5, 6, 9]:
                    ans += f(i+1, False, small or j < int(s[i]))
            return ans
        
        return f(0, True, False)
