class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = [[]]
        for i in range(len(s)):
            if s[i] == "(":
                st.append([])
            elif s[i] == ")":
                curr = st.pop()
                for c in reversed(curr):
                    st[-1].append(c)
            else:
                st[-1].append(s[i])

        return "".join(st[0])
