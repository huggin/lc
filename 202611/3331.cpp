class Solution {
public:
  vector<int> findSubtreeSizes(vector<int> &parent, string s) {
    int n = parent.size();
    vector<int> adj[n];
    for (int i = 1; i < n; ++i) {
      adj[parent[i]].push_back(i);
    }

    vector<int> ans(n);
    array<vector<int>, 26> visited;
    vector<vector<int>> new_children(n);
    function<int(int)> dfs = [&](int u) {
      visited[s[u] - 'a'].push_back(u);
      int cnt = 1;
      for (auto v : adj[u]) {
        cnt += dfs(v);
      }
      for (int v : new_children[u]) {
        cnt += ans[v];
      }
      ans[u] = cnt;
      visited[s[u] - 'a'].pop_back();
      if (visited[s[u] - 'a'].size() > 0) {
        new_children[visited[s[u] - 'a'].back()].push_back(u);
        return 0;
      } else {
        return cnt;
      }
    };
    dfs(0);
    return ans;
  }
};
