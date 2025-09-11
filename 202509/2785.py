class Solution:
    def sortVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        vos = [c for c in s if c in v]
        vos.sort()
        ans = []
        i = 0
        for c in s:
            if c in v:
                ans.append(vos[i])
                i += 1
            else:
                ans.append(c)

        return "".join(ans)
