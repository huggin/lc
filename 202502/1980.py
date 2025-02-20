class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        used = [0] * (1 << n)
        for a in nums:
            used[int(a, 2)] = 1

        for i in range(1 << n):
            if used[i] == 0:
                return bin(i)[2:].zfill(n)
        return ""
