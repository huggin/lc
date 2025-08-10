class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def digits(a):
            ans = []
            while a > 0:
                ans.append(a % 10)
                a //= 10
            return sorted(ans)
        
        a = digits(n)
        po = 1
        b = digits(po)
        while len(b) <= len(a):
            if a == b:
                return True
            po *= 2
            b = digits(po)
        return False
