class Solution {
public:
  int minScore(int n, vector<vector<int>> &roads) {
    vector<vector<pair<int, int>>> adj(n);
    for (const auto &road : roads) {
      adj[road[0] - 1].emplace_back(road[1] - 1, road[2]);
      adj[road[1] - 1].emplace_back(road[0] - 1, road[2]);
    }
    vector<int> visited(n);
    visited[0] = 1;
    queue<int> q;
    q.push(0);
    int ans = numeric_limits<int>::max();
    while (!q.empty()) {
      int u = q.front();
      visited[u] = 2;
      q.pop();
      for (const auto [v, w] : adj[u]) {
        if (visited[v] == 0) {
          visited[v] = 1;
          q.push(v);
          ans = min(ans, w);
        } else if (visited[v] == 1) {
          ans = min(ans, w);
        }
      }
    }
    return ans;
  }
};
