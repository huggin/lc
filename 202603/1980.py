class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums[0])
        for i in range(1 << n):
            
            a = f"{i:0{n}b}"
            if a not in s:
                return a
        return ""
