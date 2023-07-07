class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        def f(s, c, k):
            j = 0
            ans = 0
            for i in range(n):
                if s[i] != c:
                    k -= 1
                    while j < n and k < 0:
                        if s[j] != c:
                            k += 1
                        j += 1

                ans = max(ans, i - j + 1)
            return ans

        return max(f(answerKey, "T", k), f(answerKey, "F", k))
