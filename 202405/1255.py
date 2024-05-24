class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        n = len(words)
        cnt = [0] * 26
        for c in letters:
            cnt[ord(c) - ord("a")] += 1

        def ok(w):
            cnt2 = [0] * 26
            for c in w:
                cnt2[ord(c) - ord("a")] += 1
            for i in range(26):
                if cnt2[i] > cnt[i]:
                    return False
            return True

        @cache
        def f(k, mask):
            if k == n:
                return 0
            ans = f(k + 1, mask)
            if ok(words[k]):
                temp = 0
                for c in words[k]:
                    cnt[ord(c) - ord("a")] -= 1
                    temp += score[ord(c) - ord("a")]
                ans = max(ans, temp + f(k + 1, mask | 1 << k))
                for c in words[k]:
                    cnt[ord(c) - ord("a")] += 1
            return ans

        return f(0, 0)
