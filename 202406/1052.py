class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        ans = sum(customers[0:minutes])
        for i in range(minutes, n):
            if grumpy[i] == 0:
                ans += customers[i]

        curr = ans
        for i in range(minutes, n):
            j = i - minutes
            if grumpy[j] == 1:
                curr -= customers[j]
            if grumpy[i] == 1:
                curr += customers[i]
            ans = max(ans, curr)
        return ans
