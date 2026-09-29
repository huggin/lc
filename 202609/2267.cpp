class Solution {
public:
  bool hasValidPath(vector<vector<char>> &grid) {
    int m = grid.size();
    int n = grid[0].size();
    if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(' || (m + n) % 2 == 0)
      return false;
    vector<vector<set<int>>> dp(m, vector<set<int>>(n));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == 0 && j == 0) {
          dp[i][j].insert(1);
          continue;
        }
        if (i > 0) {
          for (int a : dp[i - 1][j]) {
            if (grid[i][j] == '(') {
              dp[i][j].insert(a + 1);
            } else if (a > 0) {
              dp[i][j].insert(a - 1);
            }
          }
        }
        if (j > 0) {
          for (int a : dp[i][j - 1]) {
            if (grid[i][j] == '(') {
              dp[i][j].insert(a + 1);
            } else if (a > 0) {
              dp[i][j].insert(a - 1);
            }
          }
        }
      }
    }
    return dp[m - 1][n - 1].find(0) != dp[m - 1][n - 1].end();
  }
};
