class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False

        left, cnt = [], []
        for i in range(len(s)):
            if locked[i] == "0":
                cnt.append(i)
            elif s[i] == ")":
                if len(left) > 0:
                    left.pop()
                elif len(cnt) > 0:
                    cnt.pop()
                else:
                    return False
            else:
                left.append(i)

        while len(left) > 0:
            if len(cnt) == 0 or left[-1] > cnt[-1]:
                return False
            left.pop()
            cnt.pop()
        return True
