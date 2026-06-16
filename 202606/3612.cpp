class Solution {
public:
  string processStr(string s) {
    string ans;
    for (const char c : s) {
      if (c == '#') {
        ans += ans;
      } else if (c == '%') {
        reverse(begin(ans), end(ans));
      } else if (c == '*') {
        if (!ans.empty()) {
          ans.pop_back();
        }
      } else {
        ans.push_back(c);
      }
    }
    return ans;
  }
};
