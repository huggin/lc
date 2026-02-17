class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            cnt = i.bit_count()
            for j in range(60):
                cnt2 = j.bit_count()
                if cnt + cnt2 == turnedOn:
                    ans.append(f"{i:d}:{j:02d}")
        return ans
