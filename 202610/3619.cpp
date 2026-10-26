class Solution {
public:
  int countIslands(vector<vector<int>> &grid, int k) {
    int m = grid.size(), n = grid[0].size();
    int ans = 0;
    int dx[4] = {-1, 0, 0, 1};
    int dy[4] = {0, -1, 1, 0};
    queue<pair<int, int>> q;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] != 0) {
          q.emplace(i, j);
          long long total = grid[i][j];
          grid[i][j] = 0;
          while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            for (int k = 0; k < 4; ++k) {
              int nx = x + dx[k];
              int ny = y + dy[k];
              if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] != 0) {
                total += grid[nx][ny];
                grid[nx][ny] = 0;
                q.emplace(nx, ny);
              }
            }
          }
          if (total % k == 0)
            ++ans;
        }
      }
    }
    return ans;
  }
};
