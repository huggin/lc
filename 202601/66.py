class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        n = len(digits)
        digits[0] += 1
        for i in range(n):
            if digits[i] != 10:
                break
            else:
                digits[i] = 0
                if i + 1 < n:
                    digits[i + 1] += 1
                else:
                    digits.append(1)
                    break
        digits.reverse()
        return digits
