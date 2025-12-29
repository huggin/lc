class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        if len(bits) == 1:
            return True
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
            else:
                i += 2
            if i == len(bits) - 1:
                return True
        return False
