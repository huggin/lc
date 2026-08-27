class Solution {
public:
  string lexGreaterPermutation(string s, string target) {
    sort(begin(s), end(s), greater<char>{});
    if (s <= target)
      return "";
    reverse(begin(s), end(s));
    string ans;
    int n = s.size();
    vector<int> used(s.size());
    int k = -1;
    for (int i = 0; i < n; ++i) {
      bool found = false;
      char bigger = '{';
      for (int j = 0; j < n; ++j) {
        if (used[j] == 1)
          continue;
        if (s[j] == target[i]) {
          used[j] = 1;
          found = true;
          ans.push_back(s[j]);
          break;
        } else if (s[j] > target[i]) {
          bigger = min(bigger, s[j]);
        }
      }
      if (!found) {
        if (bigger != '{') {
          ans.push_back(bigger);
          for (int j = 0; j < n; ++j) {
            if (used[j] == 1)
              continue;
            if (s[j] == bigger) {
              used[j] = 1;
              bigger = '{';
              continue;
            }
            if (used[j] == 0) {
              ans.push_back(s[j]);
            }
          }
          return ans;
        } else {
          k = i - 1;
          break;
        }
      }
    }
    for (int i = 0; i < n; ++i) {
      if (used[i] == 0)
        ans.push_back(s[i]);
    }
    if (k == -1)
      k = n - 2;
    char bigger = *max_element(begin(ans) + k + 1, end(ans));
    for (int i = k; i >= 0; --i) {
      if (bigger > target[i]) {
        int kk = -1;
        char b2 = '{';
        for (int k = i + 1; k < n; ++k) {
          if (b2 > ans[k] && ans[k] > target[i]) {
            b2 = ans[k];
            kk = k;
          }
        }
        swap(ans[kk], ans[i]);
        sort(begin(ans) + i + 1, end(ans));
        return ans;
      } else {
        bigger = max(bigger, ans[i]);
      }
    }
    return ans;
  }
};
