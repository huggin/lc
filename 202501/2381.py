class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        cnt = [0] * (n + 1)
        for l, r, direct in shifts:
            if direct == 0:
                direct = -1
            cnt[l] += direct
            cnt[r + 1] -= direct

        for i in range(1, n + 1):
            cnt[i] += cnt[i - 1]

        return "".join(
            chr((ord(c) - ord("a") + cnt[i] + 26) % 26 + ord("a"))
            for i, c in enumerate(s)
        )
