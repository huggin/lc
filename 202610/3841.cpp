class Fenwick {
  int n;
  vector<int> bit;

public:
  Fenwick(int m) : n(m + 1), bit(vector<int>(m + 1)) {}
  int get(int i) {
    int ans = 0;
    for (++i; i > 0; i -= i & -i) {
      ans ^= bit[i];
    }
    return ans;
  }

  void update(int i, int delta) {
    for (++i; i < n; i += i & -i) {
      bit[i] ^= delta;
    }
  }

  void update(int u, int v, int delta) {
    update(u, delta);
    update(v + 1, delta);
  }
};

class Solution {
public:
  vector<bool> palindromePath(int n, vector<vector<int>> &edges, string s,
                              vector<string> &queries) {
    vector<int> adj[n];
    for (const auto &e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }
    int l = ceil(log2(n));
    vector<int> tin(n), tout(n);
    vector<vector<int>> up(n, vector<int>(l + 1));
    int timer = -1;
    function<void(int, int)> dfs = [&](int v, int p) {
      tin[v] = ++timer;
      up[v][0] = p;
      for (int i = 1; i <= l; ++i) {
        up[v][i] = up[up[v][i - 1]][i - 1];
      }
      for (int u : adj[v]) {
        if (u != p)
          dfs(u, v);
      }
      tout[v] = ++timer;
    };

    auto is_ancestor = [&](int u, int v) -> bool {
      return tin[u] <= tin[v] && tout[u] >= tout[v];
    };

    auto lca = [&](int u, int v) -> int {
      if (is_ancestor(u, v))
        return u;
      if (is_ancestor(v, u))
        return v;
      for (int i = l; i >= 0; --i) {
        if (!is_ancestor(up[u][i], v))
          u = up[u][i];
      }
      return up[u][0];
    };

    dfs(0, 0);
    Fenwick fen(2 * n);
    for (int i = 0; i < n; ++i) {
      fen.update(tin[i], tout[i], 1 << (s[i] - 'a'));
    }
    vector<bool> ans;
    for (const auto &q : queries) {
      istringstream iss(q);
      string type;
      iss >> type;
      if (type == "update") {
        int u;
        char c;
        iss >> u >> c;
        if (s[u] != c) {
          int delta = (1 << (s[u] - 'a')) ^ (1 << (c - 'a'));
          fen.update(tin[u], tout[u], delta);
          s[u] = c;
        }
      } else {
        int u, v;
        iss >> u >> v;
        int w = lca(u, v);
        int m = fen.get(tin[u]) ^ fen.get(tin[v]) ^ (1 << s[w] - 'a');
        ans.push_back(!(m & (m - 1)));
      }
    }
    return ans;
  }
};
