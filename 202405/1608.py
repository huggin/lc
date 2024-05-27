class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            cnt = 0
            for a in nums:
                if a >= x:
                    cnt += 1

            if cnt == x:
                return x
        return -1
