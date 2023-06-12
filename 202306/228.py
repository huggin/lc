class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        start = nums[0]
        curr = 1
        n = len(nums)
        while curr < n:
            if nums[curr] > nums[curr - 1] + 1:
                end = nums[curr - 1]
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))
                start = nums[curr]
            curr += 1
        end = nums[-1]
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(end))
        
        return ans
