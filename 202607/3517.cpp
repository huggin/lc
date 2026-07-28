class Solution {
public:
  string smallestPalindrome(string s) {
    int cnt[26] = {0};
    for (char c : s) {
      ++cnt[c - 'a'];
    }
    string ans;
    char last = '$';
    for (int i = 0; i < 26; ++i) {
      if (cnt[i] > 0) {
        while (cnt[i] >= 2) {
          ans.push_back('a' + i);
          cnt[i] -= 2;
        }
        if (cnt[i] == 1) {
          last = 'a' + i;
        }
      }
    }
    string ans2(ans);
    reverse(begin(ans2), end(ans2));
    if (last != '$') {
      ans.push_back(last);
    }
    return ans + ans2;
  }
};
