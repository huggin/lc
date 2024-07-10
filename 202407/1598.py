class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for d in logs:
            if d == "../":
                if len(st) > 0:
                    st.pop()
            elif d != "./":
                st.append(d)

        return len(st)
