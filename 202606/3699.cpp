class Solution {
public:
  int zigZagArrays(int n, int l, int r) {
    int dp[2001][2001][2] = {0};
    const int MOD = int(1e9 + 7);
    for (int i = l; i <= r; ++i) {
      dp[2][i][0] = i - l;
      dp[2][i][1] = r - i;
    }
    for (int j = 3; j <= n; ++j) {
      for (int i = l + 1; i <= r; ++i) {
        dp[j - 1][i][1] = (dp[j - 1][i][1] + dp[j - 1][i - 1][1]) % MOD;
      }
      for (int i = r - 1; i >= l; --i) {
        dp[j - 1][i][0] = (dp[j - 1][i][0] + dp[j - 1][i + 1][0]) % MOD;
      }
      for (int i = l + 1; i <= r; ++i) {
        dp[j][i][0] = dp[j - 1][i - 1][1];
      }
      for (int i = r - 1; i >= l; --i) {
        dp[j][i][1] = dp[j - 1][i + 1][0];
      }
    }
    int ans = 0;
    for (int i = l; i <= r; ++i) {
      ans = (ans + dp[n][i][0]) % MOD;
      ans = (ans + dp[n][i][1]) % MOD;
    }
    return ans;
  }
};
