MOD = 10**9 + 7


@cache
def f(i, k):
    if i + k < 26:
        return 1
    ans = (f(0, k - (26 - i)) + f(1, k - (26 - i))) % MOD
    return ans


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ans = 0
        for k, v in Counter(s).items():
            ans = (ans + v * f(ord(k) - ord("a"), t)) % MOD
        return ans
