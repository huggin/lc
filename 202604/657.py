class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt1, cnt2 = 0, 0
        for m in moves:
            if m == 'U':
                cnt1 += 1
            elif m == 'D':
                cnt1 -= 1
            elif m == 'L':
                cnt2 += 1
            else:
                cnt2 -= 1
        return cnt1 == 0 and cnt2 == 0
