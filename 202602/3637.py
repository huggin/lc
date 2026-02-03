class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 3:
            return False
        if nums[1] <= nums[0]:
            return False
        for i in range(2, n):
            if nums[i] == nums[i-1]:
                return False
        cnt = 0
        i = 0
        flag = 1
        while i < n:
            j = i + 1
            while j < n and (nums[j] - nums[j-1]) * flag > 0:
                j += 1
            if j != n:
                cnt += 1
                if cnt > 2:
                    return False
                flag *= -1
            i = j
                
        return cnt == 2
