class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for c in num:
            while len(st) > 0 and ord(c) < ord(st[-1]) and k > 0:
                st.pop()
                k -= 1
            st.append(c)

        while k > 0 and len(st) > 0:
            st.pop()
            k -= 1

        j = 0
        while j < len(st) and st[j] == "0":
            j += 1

        return "".join(st[j:]) if j < len(st) else "0"
