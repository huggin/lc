class Solution {
public:
  vector<vector<int>> shiftGrid(vector<vector<int>> &grid, int k) {
    auto move = [](vector<vector<int>> &g) {
      int m = g.size();
      int n = g[0].size();
      int temp = g[m - 1][n - 1];
      for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 1; --j) {
          g[i][j] = g[i][j - 1];
        }
        if (i != 0) {
          g[i][0] = g[i - 1][n - 1];
        } else {
          g[i][0] = temp;
        }
      }
    };

    for (int i = 0; i < k; ++i) {
      move(grid);
    }
    return grid;
  }
};
