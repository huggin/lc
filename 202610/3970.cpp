class Solution {
public:
  int shortestPath(int n, vector<vector<int>> &edges, string labels, int k) {
    vector<pair<int, int>> adj[n];
    for (auto &e : edges) {
      adj[e[0]].emplace_back(e[1], e[2]);
    }
    using PQ =
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>,
                       greater<tuple<int, int, int>>>;
    PQ pq;
    pq.emplace(0, 0, 1);
    vector<unordered_map<int, int>> dist(n);
    while (!pq.empty()) {
      auto [d, u, c] = pq.top();
      pq.pop();
      if (dist[u].find(c) != dist[u].end() && dist[u][c] <= d)
        continue;
      dist[u][c] = d;
      for (const auto [v, w] : adj[u]) {
        if (labels[u] == labels[v]) {
          if (k == c)
            continue;
          pq.emplace(d + w, v, c + 1);
        } else {
          pq.emplace(d + w, v, 1);
        }
      }
    }
    int ans = INT_MAX;
    for (auto [k, v] : dist[n - 1]) {
      ans = min(ans, v);
    }
    return ans == INT_MAX ? -1 : ans;
  }
};
