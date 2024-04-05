class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for c in s:
            if len(st) > 0 and st[-1] != c and c.lower() == st[-1].lower():
                st.pop()
            else:
                st.append(c)

        return "".join(st)
