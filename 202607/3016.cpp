class Solution {
public:
  int minimumPushes(string word) {
    vector<int> cnt(26);
    for (char c : word) {
      ++cnt[c - 'a'];
    }
    sort(begin(cnt), end(cnt));
    int ans = 0;
    int j = 0;
    int press = 0;
    for (int i = 25; i >= 0; --i) {
      if (cnt[i] == 0)
        break;
      if ((j++ % 8) == 0) {
        ++press;
      }
      ans += press * cnt[i];
    }
    return ans;
  }
};
