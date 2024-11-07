class Solution:
    def largestCombination(self, cs: List[int]) -> int:
        cnt = [0] * 32

        for c in cs:
            for i in range(32):
                if c & (1 << i):
                    cnt[i] += 1

        return max(cnt)
