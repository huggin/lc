class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        C = Counter(answers)
        ans = 0
        for k, v in C.items():
            ans += (v + k) // (k + 1) * (k + 1)
        return ans
