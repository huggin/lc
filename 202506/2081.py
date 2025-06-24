class Solution:
    def kMirror(self, k: int, n: int) -> int:
        ans = 0
        start = 1
        end = 10

        def construct(a):
            s = str(a)
            return s + s[-2::-1]

        def construct2(a):
            s = str(a)
            return s + s[-1::-1]

        def ok(s):
            digit = []
            while s > 0:
                digit.append(s % k)
                s //= k
            m = len(digit)
            for i in range(m // 2 + 1):
                if digit[i] != digit[m - 1 - i]:
                    return False
            return True

        while n > 0:
            for i in range(start, end):
                s = int(construct(i))
                if ok(s):
                    ans += s
                    n -= 1
                    if n == 0:
                        return ans

            for i in range(start, end):
                s = int(construct2(i))
                if ok(s):
                    ans += s
                    n -= 1
                    if n == 0:
                        return ans

            start *= 10
            end *= 10

        return ans
