class Solution {
public:
  int numberOfSubstrings(string s) {
    int cnt[3] = {0};
    int j = 0;
    int ans = 0;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
      cnt[s[i] - 'a']++;
      while (cnt[0] > 0 && cnt[1] > 0 && cnt[2] > 0) {
        ans += n - i;
        if (j < i) {
          cnt[s[j] - 'a']--;
          j++;
        }
      }
    }
    return ans;
  }
};
