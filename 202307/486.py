class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def f(i, j, player):
            if i > j:
                return 0
            
            return max(nums[i] - f(i+1, j, 1-player), nums[j] - f(i, j-1, 1-player))
            
        return f(0, n-1, 0) >= 0
            
