class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        def f(a):
            j = -1
            mi = float("inf")
            for i in range(len(a) - 1):
                if nums[i] + nums[i + 1] < mi:
                    mi = nums[i] + nums[i + 1]
                    j = i
            return a[0:j] + [mi] + a[j + 2 :]

        while True:
            flag = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    flag = False
                    break
            if flag:
                break
            nums = f(nums)
        return n - len(nums)
