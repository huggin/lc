class Solution:
    def findLucky(self, arr: List[int]) -> int:
        C = Counter(arr)
        ans = -1
        for k, v in C.items():
            if k == v:
                ans = max(ans, v)
        return ans
