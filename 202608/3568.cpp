class Solution {
public:
  int minMoves(vector<string> &classroom, int energy) {
    int m = classroom.size();
    int n = classroom[0].size();
    vector<vector<int>> idx(m, vector<int>(n));

    int curr = 0;
    int x = -1, y = -1;
    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (classroom[i][j] == 'L') {
          idx[i][j] = curr++;
        } else if (classroom[i][j] == 'S') {
          x = i;
          y = j;
        }
      }
    }
    int mask = (1 << curr) - 1;
    vector<vector<vector<int>>> best(
        m, vector<vector<int>>(n, vector<int>(mask + 1)));
    queue<tuple<int, int, int, int, int>> q;
    q.emplace(x, y, mask, energy, 0);
    while (!q.empty()) {
      auto [x, y, mask, e, step] = q.front();
      if (mask == 0)
        return step;
      q.pop();
      if (classroom[x][y] == 'R') {
        e = energy;
      }
      if (e == 0)
        continue;
      if (best[x][y][mask] >= e)
        continue;
      best[x][y][mask] = e;
      for (int k = 0; k < 4; ++k) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx < 0 || nx >= m || ny < 0 || ny >= n || classroom[nx][ny] == 'X')
          continue;
        int new_mask = mask;
        if (classroom[nx][ny] == 'L') {
          new_mask = mask & ~(1 << idx[nx][ny]);
        }
        q.emplace(nx, ny, new_mask, e - 1, step + 1);
      }
    }
    return -1;
  }
};
