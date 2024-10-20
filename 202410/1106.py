class Solution:
    def parseBoolExpr(self, e: str) -> bool:
        def expr(i, j):
            if i == j:
                return True if e[i] == "t" else False
            if e[i] == "!":
                return not expr(i + 2, j - 1)
            if e[i] == "&":
                ans = True
                k = i + 2
                i += 2
                cnt = 0
                while k < j:
                    if e[k] == "(":
                        cnt += 1
                    elif e[k] == ")":
                        cnt -= 1
                    elif e[k] == ",":
                        if cnt == 0:
                            ans = ans and expr(i, k - 1)
                            i = k + 1
                    k += 1
                ans = ans and expr(i, j - 1)
                return ans

            if e[i] == "|":
                ans = False
                k = i + 2
                i += 2
                cnt = 0
                while k < j:
                    if e[k] == "(":
                        cnt += 1
                    elif e[k] == ")":
                        cnt -= 1
                    elif e[k] == ",":
                        if cnt == 0:
                            ans = ans or expr(i, k - 1)
                            i = k + 1
                    k += 1
                ans = ans or expr(i, j - 1)
                return ans
            return False

        return expr(0, len(e) - 1)
