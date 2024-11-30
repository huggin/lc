class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        ind = defaultdict(int)
        oud = defaultdict(int)
        v = set()
        idx = defaultdict(int)

        for x, y in pairs:
            g[x].append(y)
            ind[y] += 1
            oud[x] += 1
            v.add(x)
            v.add(y)

        start, end = -1, -1
        for x in v:
            if ind[x] - oud[x] == 1:
                end = x
            elif oud[x] - ind[x] == 1:
                start = x

        if start == -1:
            start, end = pairs[0][0], pairs[0][0]

        st = []
        vs = []
        st.append(start)
        while st:
            i = st[-1]
            if idx[i] == len(g[i]):
                vs.append(i)
                st.pop()
            else:
                st.append(g[i][idx[i]])
                idx[i] += 1

        ans = []
        for i in range(len(vs) - 1, 0, -1):
            ans.append([vs[i], vs[i - 1]])
        return ans
