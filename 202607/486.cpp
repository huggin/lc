class Solution {
public:
  bool predictTheWinner(vector<int> &nums) {
    vector<vector<int>> dp(nums.size(), vector<int>(nums.size(), -1));
    function<int(int, int)> f = [&](int i, int j) {
      if (i > j)
        return 0;
      if (dp[i][j] != -1)
        return dp[i][j];
      return dp[i][j] = max(nums[i] - f(i + 1, j), nums[j] - f(i, j - 1));
    };
    return f(0, nums.size() - 1) >= 0;
  }
};
