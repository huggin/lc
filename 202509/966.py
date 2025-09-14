class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        normalized = {}
        v = {}

        @cache
        def getv(l):
            t = []
            for c in l:
                if c in "aeiou":
                    t.append("$")
                else:
                    t.append(c)
            return "".join(t)

        for w in wordlist:
            l = w.lower()
            if l not in normalized:
                normalized[l] = w

            t = getv(l)
            if t not in v:
                v[t] = w

        ans = []
        for w in queries:
            if w in words:
                ans.append(w)
            else:
                l = w.lower()
                if l in normalized:
                    ans.append(normalized[l])
                else:
                    t = getv(l)
                    if t in v:
                        ans.append(v[t])
                    else:
                        ans.append("")

        return ans
