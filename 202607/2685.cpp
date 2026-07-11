class Solution {
public:
  int countCompleteComponents(int n, vector<vector<int>> &edges) {
    vector<vector<int>> adj(n);
    for (const auto &edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
    }
    vector<int> visited(n);
    auto bfs = [&](int v) -> pair<int, int> {
      queue<int> q;
      q.push(v);
      visited[v] = 1;
      int node = 0, edge = 0;
      while (!q.empty()) {
        int u = q.front();
        ++node;
        q.pop();
        edge += adj[u].size();
        for (int w : adj[u]) {
          if (!visited[w]) {
            visited[w] = 1;
            q.push(w);
          }
        }
      }
      return {node, edge};
    };
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (!visited[i]) {
        auto [node, edge] = bfs(i);
        if (node * (node - 1) == edge) {
          ++ans;
        }
      }
    }
    return ans;
  }
};
