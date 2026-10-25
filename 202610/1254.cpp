class Solution {
public:
  int closedIsland(vector<vector<int>> &grid) {
    int dx[4] = {-1, 0, 0, 1};
    int dy[4] = {0, -1, 1, 0};
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> q;
    for (int i = 0; i < n; ++i) {
      if (grid[0][i] == 0) {
        q.emplace(0, i);
        grid[0][i] = 2;
      }
      if (grid[m - 1][i] == 0) {
        q.emplace(m - 1, i);
        grid[m - 1][i] = 2;
      }
    }
    for (int i = 0; i < m; ++i) {
      if (grid[i][0] == 0) {
        q.emplace(i, 0);
        grid[i][0] = 2;
      }
      if (grid[i][n - 1] == 0) {
        q.emplace(i, n - 1);
        grid[i][n - 1] = 2;
      }
    }
    while (!q.empty()) {
      auto [x, y] = q.front();
      q.pop();
      for (int k = 0; k < 4; ++k) {
        int nx = x + dx[k], ny = y + dy[k];
        if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 0) {
          q.emplace(nx, ny);
          grid[nx][ny] = 2;
        }
      }
    }
    int ans = 0;
    for (int i = 1; i < m - 1; ++i) {
      for (int j = 1; j < n - 1; ++j) {
        if (grid[i][j] == 0) {
          ++ans;
          q.emplace(i, j);
          grid[i][j] = 2;
        }
        while (!q.empty()) {
          auto [x, y] = q.front();
          q.pop();
          for (int k = 0; k < 4; ++k) {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 0) {
              q.emplace(nx, ny);
              grid[nx][ny] = 2;
            }
          }
        }
      }
    }
    return ans;
  }
};
