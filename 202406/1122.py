class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ans = []
        for a in arr2:
            ans += [a] * c[a]

        s = set(arr2)
        ans2 = []
        for a in arr1:
            if a in s:
                continue
            ans2.append(a)
        return ans + sorted(ans2)
