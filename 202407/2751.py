class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        a = []
        n = len(positions)
        for i in range(n):
            a.append([positions[i], healths[i], 1 if directions[i] == 'L' else 0, i])
        
        a.sort(key = lambda x : x[0])
        st = []
        for c in a:
            flag = True
            while c[2] == 1 and len(st) > 0 and st[-1][2] == 0:
                if st[-1][1] > c[1]:
                    st[-1][1] -= 1
                    flag = False
                    break
                elif st[-1][1] == c[1]:
                    st.pop()
                    flag = False
                    break
                else:
                    st.pop()
                    c[1] -= 1
            if flag:
                st.append(c)
        
        st.sort(key = lambda x : x[3])
            
        return [c[1] for c in st]
