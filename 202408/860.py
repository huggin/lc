class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten == 0 and five <= 2 or five == 0:
                    return False
                if ten == 0:
                    five -= 3
                else:
                    five -= 1
                    ten -= 1
        return True
