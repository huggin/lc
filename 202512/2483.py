class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr = customers.count("Y")
        n = len(customers)
        ans = 0
        ansv = curr
        for i in range(1, n + 1):
            if customers[i - 1] == "Y":
                curr -= 1
            else:
                curr += 1
            if ansv > curr:
                curr = ansv
                ans = i
        return ans
