class Solution {
public:
  int maxActiveSectionsAfterTrade(string s) {
    vector<pair<int, int>> segs;
    for (char c : s) {
      if (segs.size() == 0 || segs.back().second != c - '0') {
        segs.emplace_back(1, c - '0');
      } else {
        ++segs.back().first;
      }
    }
    int ans = 0;
    vector<int> zeroes;

    for (int i = 0; i < segs.size(); ++i) {
      if (segs[i].second == 1) {
        ans += segs[i].first;
      } else {
        zeroes.push_back(segs[i].first);
      }
    }
    if (zeroes.size() <= 1)
      return ans;
    int ma = 0;
    for (int i = 1; i < zeroes.size(); ++i) {
      ma = max(ma, zeroes[i] + zeroes[i - 1]);
    }
    return ans + ma;
  }
};
