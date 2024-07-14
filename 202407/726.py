class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = '(' + formula + ')'
        st = []
        i = 0
        while i < len(formula):
            if formula[i].isupper():
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                atom = formula[i:j]
                i = j
                cnt = 0
                while i < len(formula) and formula[i].isdigit():
                    cnt = cnt * 10 + int(formula[i])
                    i += 1
                if cnt == 0:
                    cnt = 1
                st[-1][atom] += cnt
            elif formula[i] == '(':
                st.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                cnt = 0
                i += 1
                while i < len(formula) and formula[i].isdigit():
                    cnt = cnt * 10 + int(formula[i])
                    i += 1
                if cnt == 0:
                    cnt = 1
                
                if len(st) > 1:
                    last = st.pop()
                    for k, v in last.items():  
                        st[-1][k] += cnt * v

        ans = ""
        for k in sorted(st[0].keys()):
            if st[0][k] == 1:
                ans += k
            else:
                ans += '{}{}'.format(k, st[0][k])
        return ans
                

