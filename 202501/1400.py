class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        odd = sum(c % 2 for c in cnt)
        return odd <= k and len(s) >= k
