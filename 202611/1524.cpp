class Solution {
public:
  int numOfSubarrays(vector<int> &arr) {
    const int MOD = 1e9 + 7;
    int n = arr.size();
    vector<vector<int>> dp(2, vector<int>(n + 1));
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (arr[i] % 2) {
        dp[1][i + 1] = 1 + dp[0][i];
        dp[0][i + 1] = dp[1][i];
      } else {
        dp[1][i + 1] = dp[1][i];
        dp[0][i + 1] = 1 + dp[0][i];
      }
      ans += dp[1][i + 1];
      if (ans >= MOD)
        ans -= MOD;
    }
    return ans;
  }
};
