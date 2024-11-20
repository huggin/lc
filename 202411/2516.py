class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3
        for c in s:
            cnt[ord(c) - 97] += 1

        for i in range(3):
            if cnt[i] < k:
                return -1

        n = len(s)
        cnt2 = [0] * 3

        ans = 0
        j = 0
        for i in range(n):
            cnt2[ord(s[i]) - 97] += 1
            while cnt2[0] + k > cnt[0] or cnt2[1] + k > cnt[1] or cnt2[2] + k > cnt[2]:
                cnt2[ord(s[j]) - 97] -= 1
                j += 1

            ans = max(ans, i - j + 1)

        return n - ans
