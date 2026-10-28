class Solution {
public:
  int minCost(vector<vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<vector<int>>> dp(m,
                                   vector<vector<int>>(n, vector<int>(1024)));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == 0 && j == 0) {
          dp[0][0][grid[0][0]] = 1;
          continue;
        }
        for (int k = 0; k < 1024; ++k) {
          if (i > 0) {
            if (dp[i - 1][j][k] == 1) {
              dp[i][j][k ^ grid[i][j]] = 1;
            }
          }
          if (j > 0) {
            if (dp[i][j - 1][k] == 1) {
              dp[i][j][k ^ grid[i][j]] = 1;
            }
          }
        }
      }
    }
    for (int i = 0; i < 1024; ++i) {
      if (dp[m - 1][n - 1][i])
        return i;
    }
    return -1;
  }
};
