class Solution {
public:
  int uniquePaths(vector<vector<int>> &grid) {
    const int MOD = 1e9 + 7;
    int m = grid.size(), n = grid[0].size();
    int dp[500][500][2] = {0};
    dp[0][0][0] = 1;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0) {
          int tt = dp[i][j][0] + dp[i][j][1];
          if (i < m - 1) {
            dp[i + 1][j][0] = (dp[i + 1][j][0] + tt) % MOD;
          }
          if (j < n - 1) {
            dp[i][j + 1][1] = (dp[i][j + 1][1] + tt) % MOD;
          }
        } else {
          if (i < m - 1) {
            dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][1]) % MOD;
          }
          if (j < n - 1) {
            dp[i][j + 1][1] = (dp[i][j + 1][1] + dp[i][j][0]) % MOD;
          }
        }
      }
    }
    return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD;
  }
};
