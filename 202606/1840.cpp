class Solution {
public:
  int maxBuilding(int n, vector<vector<int>> &restrictions) {
    if (restrictions.empty()) {
      return n - 1;
    }
    restrictions.emplace_back(1, 0);
    sort(begin(restrictions), end(restrictions));
    vector<pair<int, int>> vp;
    vp.emplace_back(1, 0);
    for (int i = 1; i < restrictions.size(); ++i) {
      vp.emplace_back(
          restrictions[i][0],
          min(restrictions[i][0] - vp.back().first + vp.back().second,
              restrictions[i][1]));
    }
    for (int i = vp.size() - 2; i >= 0; --i) {
      vp[i].second =
          min(vp[i + 1].second + vp[i + 1].first - vp[i].first, vp[i].second);
    }
    int ans = vp.back().second + n - vp.back().first;
    for (int i = 1; i < vp.size(); ++i) {
      ans = max(ans, vp[i].second);
      if (vp[i].first - vp[i - 1].first > vp[i].second - vp[i - 1].second) {
        ans = max(ans, max(vp[i].second, vp[i - 1].second) +
                           (vp[i].first - vp[i - 1].first -
                            abs(vp[i].second - vp[i - 1].second)) /
                               2);
      }
    }

    return ans;
  }
};
