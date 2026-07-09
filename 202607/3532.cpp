class Solution {
public:
  vector<bool> pathExistenceQueries(int n, vector<int> &nums, int maxDiff,
                                    vector<vector<int>> &queries) {
    vector<pair<int, int>> a;
    for (auto const &[i, v] : std::views::enumerate(nums)) {
      a.emplace_back(v, i);
    }
    sort(begin(a), end(a));
    vector<int> groups(n, -1);
    groups[a[0].second] = 0;
    for (int i = 1; i < n; ++i) {
      if (a[i].first - a[i - 1].first <= maxDiff) {
        groups[a[i].second] = groups[a[i - 1].second];
      } else {
        groups[a[i].second] = groups[a[i - 1].second] + 1;
      }
    }
    vector<bool> ans;
    for (auto const &q : queries) {
      ans.push_back(groups[q[0]] == groups[q[1]]);
    }
    return ans;
  }
};
