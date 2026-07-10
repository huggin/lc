class Solution {
public:
  vector<int> pathExistenceQueries(int n, vector<int> &nums, int maxDiff,
                                   vector<vector<int>> &queries) {
    int log = int(log2(n));
    vector<vector<int>> dp(log + 1, vector<int>(n));
    vector<pair<int, int>> a;
    for (int i = 0; i < nums.size(); ++i) {
      a.emplace_back(nums[i], i);
    }
    sort(a.begin(), a.end());
    vector<int> pos(n);
    vector<int> group(n);
    int cg = 0;
    for (int i = 0; i < n; ++i) {
      pos[a[i].second] = i;
    }
    for (int i = 1; i < n; ++i) {
      if (a[i].first - a[i - 1].first > maxDiff) {
        ++cg;
      }
      group[i] = cg;
    }
    vector<int> nxt(n);
    int j = 0;
    for (int i = 0; i < n; ++i) {
      while (j + 1 < n && a[j + 1].first - a[i].first <= maxDiff) {
        ++j;
      }
      nxt[i] = j;
    }
    dp[0] = nxt;
    for (int i = 1; i <= log; ++i) {
      for (int j = 0; j < n; ++j) {
        dp[i][j] = dp[i - 1][dp[i - 1][j]];
      }
    }

    vector<int> ans(queries.size(), -1);
    for (int i = 0; i < queries.size(); ++i) {
      int u = pos[queries[i][0]];
      int v = pos[queries[i][1]];
      if (group[u] == group[v]) {
        if (u > v)
          swap(u, v);
        if (u == v) {
          ans[i] = 0;
        } else {
          int jump = 0;
          for (int j = log; j >= 0; --j) {
            if (dp[j][u] < v) {
              jump += 1 << j;
              u = dp[j][u];
            }
          }
          ans[i] = jump + 1;
        }
      }
    }
    return ans;
  }
};
