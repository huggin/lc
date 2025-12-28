class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        curr = 0
        for level in bank:
            n = level.count("1")
            if n == 0:
                continue
            ans += curr * n
            curr = n
        return ans
