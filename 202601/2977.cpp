class Solution {
public:
  long long minimumCost(string source, string target, vector<string> &original,
                        vector<string> &changed, vector<int> &cost) {
    const long long INF = (long long)1e18;
    int n = original.size();

    unordered_map<string, int> id;
    int idx = 0;

    auto getId = [&](const string &s) {
      if (!id.count(s))
        id[s] = idx++;
      return id[s];
    };

    for (int i = 0; i < n; i++) {
      getId(original[i]);
      getId(changed[i]);
    }

    vector<vector<long long>> g(idx, vector<long long>(idx, INF));
    for (int i = 0; i < idx; i++)
      g[i][i] = 0;

    for (int i = 0; i < n; i++) {
      int u = id[original[i]];
      int v = id[changed[i]];
      g[u][v] = min(g[u][v], (long long)cost[i]);
    }

    for (int k = 0; k < idx; k++) {
      for (int i = 0; i < idx; i++) {
        for (int j = 0; j < idx; j++) {
          if (g[i][k] < INF && g[k][j] < INF) {
            g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
          }
        }
      }
    }

    unordered_map<int, unordered_map<string_view, int>> bucket;

    for (auto &[s, i] : id) {
      bucket[s.size()][string_view(s)] = i;
    }

    vector<int> lens;
    for (auto &[l, _] : bucket)
      lens.push_back(l);
    sort(lens.begin(), lens.end());

    int m = source.size();
    vector<long long> dp(m + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < m; i++) {
      if (source[i] == target[i]) {
        dp[i + 1] = min(dp[i + 1], dp[i]);
      }

      for (int l : lens) {
        if (i - l + 1 < 0)
          continue;

        string_view s1(source.data() + i - l + 1, l);
        string_view s2(target.data() + i - l + 1, l);

        auto it1 = bucket[l].find(s1);
        auto it2 = bucket[l].find(s2);
        if (it1 == bucket[l].end() || it2 == bucket[l].end())
          continue;

        dp[i + 1] = min(dp[i + 1], dp[i - l + 1] + g[it1->second][it2->second]);
      }
    }

    return dp[m] < INF ? dp[m] : -1;
  }
};
