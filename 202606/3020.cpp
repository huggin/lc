class Solution {
public:
  int maximumLength(vector<int> &nums) {
    unordered_map<long long, int> m;
    for (int c : nums) {
      m[c]++;
    }
    int ans = m[1] & 1 ? m[1] : m[1] ? m[1] - 1 : 0;
    for (const auto [k, v] : m) {
      if (k == 1)
        continue;
      if (v >= 2) {
        long long s = k;
        int cnt = 0;
        while (m.find(s) != m.end() && m[s] >= 2) {
          ++cnt;
          s *= s;
        }
        if (m.find(s) != m.end()) {
          ans = max(cnt * 2 + 1, ans);
        } else {
          ans = max(cnt * 2 - 1, ans);
        }
      } else {
        ans = max(ans, 1);
      }
    }
    return ans;
  }
};
