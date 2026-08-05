class Solution {
public:
  vector<int> remainingMethods(int n, int k, vector<vector<int>> &invocations) {
    vector<vector<int>> adj(n);
    for (const auto &inv : invocations) {
      adj[inv[0]].push_back(inv[1]);
    }
    vector<int> visited(n);
    visited[k] = 1;
    queue<int> q;
    q.push(k);
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      for (int v : adj[u]) {
        if (!visited[v]) {
          visited[v] = 1;
          q.push(v);
        }
      }
    }
    vector<int> ans(n);
    std::iota(ans.begin(), ans.end(), 0);
    vector<int> ans2;
    for (int i = 0; i < n; ++i) {
      if (!visited[i]) {
        for (int v : adj[i]) {
          if (visited[v]) {
            return ans;
          }
        }
        ans2.push_back(i);
      }
    }
    return ans2;
  }
};
