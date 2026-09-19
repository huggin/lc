class Solution {
public:
  vector<string> maxNumOfSubstrings(string s) {
    vector<int> a[26];
    for (auto [i, c] : std::views::enumerate(s)) {
      a[c - 'a'].push_back(i);
    }
    vector<pair<int, int>> subs;
    for (int i = 0; i < 26; ++i) {
      if (a[i].empty())
        continue;
      int left = a[i].front();
      int right = a[i].back();
      bool flag = true;
      while (flag) {
        flag = false;
        for (int j = 0; j < 26; ++j) {
          if (i == j || a[j].empty())
            continue;
          if (left <= a[j].front() && a[j].back() <= right)
            continue;
          if (lower_bound(begin(a[j]), end(a[j]), left) !=
              lower_bound(begin(a[j]), end(a[j]), right)) {
            left = min(left, a[j].front());
            right = max(right, a[j].back());
            flag = true;
            break;
          }
        }
      }
      subs.emplace_back(left, right - left + 1);
    }
    if (subs.size() == 0)
      return {s};

    sort(begin(subs), end(subs),
         [](const auto l, const auto r) { return l.second < r.second; });
    vector<string> ans;
    vector<pair<int, int>> used;
    for (int i = 0; i < subs.size(); ++i) {
      bool found = true;
      for (int j = 0; j < used.size(); ++j) {
        if (subs[i].first <= used[j].first &&
            used[j].first < subs[i].first + subs[i].second) {
          found = false;
          break;
        }
      }
      if (found) {
        ans.push_back(s.substr(subs[i].first, subs[i].second));
        used.emplace_back(subs[i]);
      }
    }

    return ans;
  }
};
