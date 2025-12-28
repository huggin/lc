from functools import cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def f(i, j, mask):
            if i == n:
                return 1

            if j == 0:
                nm = mask | 1 << ord(s[i]) - ord("a")
                if nm.bit_count() > k:
                    return 1 + f(i, 0, 0)
                else:
                    return f(i + 1, 0, nm)
            else:
                ans = 1
                for c in range(26):
                    if c == ord(s[i]) - ord("a"):
                        nm = mask | 1 << c
                        if nm.bit_count() > k:
                            ans = max(ans, 1 + f(i + 1, 1, 1 << c))
                        else:
                            ans = max(ans, f(i + 1, 1, nm))
                        continue
                    nm = mask | 1 << c
                    if nm.bit_count() > k:
                        ans = max(ans, 1 + f(i + 1, 0, 1 << c))
                    else:
                        ans = max(ans, f(i + 1, 0, nm))
                return ans

        return f(0, 1, 0)
