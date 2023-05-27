class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = senate
        cnt = 0
        while True:
            ns = ""
            r, d = 0, 0
            for i in range(len(s)):
                if s[i] == "R":
                    cnt += 1
                    if cnt <= 0:
                        continue
                    else:
                        ns += "R"
                        r += 1
                else:
                    cnt -= 1
                    if cnt >= 0:
                        continue
                    else:
                        ns += "D"
                        d += 1

            if r >= 2 * d:
                return "Radiant"
            elif d >= 2 * r:
                return "Dire"
            s = ns

        return "Fuck"
