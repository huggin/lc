class Solution {
public:
  vector<int> maximumWeight(vector<vector<int>> &intervals) {
    int n = intervals.size();
    vector<vector<long long>> dp(n + 1, vector<long long>(5));
    vector<vector<vector<int>>> dp2(n + 1, vector<vector<int>>(5));
    vector<tuple<int, int, int, int>> a;
    for (const auto &[k, v] : views::enumerate(intervals)) {
      a.emplace_back(v[0], v[1], v[2], k);
    }
    sort(begin(a), end(a),
         [](auto &&l, auto &&r) { return get<1>(l) < get<1>(r); });
    for (int i = 0; i < n; ++i) {
      auto [l, r, w, idx] = a[i];
      int k = lower_bound(a.begin(), a.begin() + i, l,
                          [](const auto &t, int v) { return get<1>(t) < v; }) -
              a.begin();
      for (int j = 1; j <= 4; ++j) {
        long long s1 = dp[i][j];
        long long s2 = dp[k][j - 1] + w;
        if (s1 > s2) {
          dp[i + 1][j] = dp[i][j];
          dp2[i + 1][j] = dp2[i][j];
        } else {
          vector<int> np(dp2[k][j - 1]);
          np.push_back(idx);
          sort(np.begin(), np.end());
          if (s1 == s2 && dp2[i][j] < np) {
            np = dp2[i][j];
          }
          dp[i + 1][j] = s2;
          dp2[i + 1][j] = np;
        }
      }
    }
    return dp2[n][4];
  }
};
