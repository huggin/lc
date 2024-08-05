class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for a in arr:
            if c[a] != 1:
                continue
            k -= 1
            if k == 0:
                return a
        return ""
