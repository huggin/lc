class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        seen = defaultdict(int)
        for w in words:
            if seen[w[::-1]] > 0:
                ans += 4
                seen[w[::-1]] -= 1
            else:
                seen[w] += 1

        for k, v in seen.items():
            if v != 0 and k[0] == k[1]:
                ans += 2
                break
        return ans
