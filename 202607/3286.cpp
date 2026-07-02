class Solution {
public:
  bool findSafeWalk(vector<vector<int>> &grid, int health) {
    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};
    deque<pair<int, int>> q;
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dist(m, vector<int>(n));
    q.emplace_back(0, 0);
    dist[0][0] = health - grid[0][0];
    if (dist[0][0] == 0)
      return false;
    while (!q.empty()) {
      auto [i, j] = q.front();
      q.pop_front();
      if (dist[i][j] <= 0)
        continue;
      for (int k = 0; k < 4; ++k) {
        int ni = i + dx[k];
        int nj = j + dy[k];
        if (ni >= 0 && ni < m && nj >= 0 && nj < n && dist[ni][nj] == 0) {
          if (grid[ni][nj] == 1) {
            q.emplace_back(ni, nj);
            dist[ni][nj] = dist[i][j] - 1;
          } else {
            q.emplace_front(ni, nj);
            dist[ni][nj] = dist[i][j];
          }
        }
      }
    }
    return dist[m - 1][n - 1] > 0;
  }
};
