class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right = {}
        for k, c in enumerate(s):
            right[c] = k
        
        ans = []
        n = len(s)
        j = 0
        while j < n:
            ma = right[s[j]]
            i = j
            while i < ma:
                ma = max(ma, right[s[i]])
                i += 1
            ans.append(i - j + 1)
            j = i + 1

        return ans
