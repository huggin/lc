class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def f(a, b, x, y):
            st = []
            ans = 0
            for c in s:
                if c == b:
                    if len(st) > 0 and st[-1] == a:
                        ans += x
                        st.pop()
                    else:
                        st.append(c)
                else:
                    st.append(c)

            st2 = []
            for c in st:
                if c == a:
                    if len(st2) > 0 and st2[-1] == b:
                        ans += y
                        st2.pop()
                    else:
                        st2.append(c)
                else:
                    st2.append(c)
            return ans

        if x > y:
            return f("a", "b", x, y)
        else:
            return f("b", "a", y, x)
