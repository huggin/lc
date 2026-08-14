class Solution {
public:
  int maximumLengthSubstring(string s) {
    array<int, 26> cnt;
    int j = 0, ans = 0;
    for (int i = 0; i < s.size(); ++i) {
      ++cnt[s[i] - 'a'];
      while (cnt[s[i] - 'a'] > 2) {
        --cnt[s[j++] - 'a'];
      }
      ans = max(ans, i - j + 1);
    }
    return ans;
  }
};
