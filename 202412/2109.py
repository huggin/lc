class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a = []
        j = 0
        for i in spaces:
            a.append(s[j:i])
            j = i
        a.append(s[j:])
        return " ".join(a)
