class Solution {
public:
  string smallestSubsequence(string s) {
    array<int, 26> cnt{};
    array<bool, 26> used{};

    for (char c : s) {
      ++cnt[c - 'a'];
    }

    string ans;
    for (char c : s) {
      --cnt[c - 'a'];

      if (used[c - 'a']) {
        continue;
      }

      while (!ans.empty() && ans.back() > c && cnt[ans.back() - 'a'] > 0) {
        used[ans.back() - 'a'] = false;
        ans.pop_back();
      }

      ans.push_back(c);
      used[c - 'a'] = true;
    }

    return ans;
  }
};
