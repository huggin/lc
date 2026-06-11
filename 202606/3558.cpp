class Solution {
  vector<vector<int>> adj;
  int depth(int v, int p = -1) {
    int ans = 0;
    for (const int u : adj[v]) {
      if (u != p) {
        ans = max(ans, 1 + depth(u, v));
      }
    }
    return ans;
  }
  int exp(int n) {
    long long ans = 1;
    const int MOD = int(1e9 + 7);
    long long b = 2;
    while (n > 0) {
      if (n & 1) {
        ans *= b;
        ans %= MOD;
      }
      b = b * b;
      b %= MOD;
      n >>= 1;
    }
    return ans;
  }

public:
  int assignEdgeWeights(vector<vector<int>> &edges) {
    int n = edges.size() + 1;
    adj.resize(n);
    for (const auto &edge : edges) {
      adj[edge[0] - 1].push_back(edge[1] - 1);
      adj[edge[1] - 1].push_back(edge[0] - 1);
    }
    int md = depth(0, -1);
    return exp(md - 1);
  }
};
