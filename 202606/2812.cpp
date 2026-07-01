class Solution {
public:
  int maximumSafenessFactor(vector<vector<int>> &grid) {
    int n = grid.size();
    queue<pair<int, int>> q;
    vector<vector<int>> safe(n, vector<int>(n, -1));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          safe[i][j] = 0;
          q.emplace(i, j);
        }
      }
    }
    int dx[] = {-1, 0, 0, 1};
    int dy[] = { 0, -1, 1, 0… auto [d, i, j] = pq.top();
    pq.pop();
    if (d < dist[i][j])
      continue;
    for (int k = 0; k < 4; ++k) {
      int ni = i + dx[k];
      int nj = j + dy[k];
      if (ni >= 0 && ni < n && nj >= 0 && nj < n &&
          dist[ni][nj] < min(d, safe[ni][nj])) {
        dist[ni][nj] = min(d, safe[ni][nj]);
        pq.emplace(dist[ni][nj], ni, nj);
      }
    }
  }
  return dist[n - 1][n - 1];
}
}
;
