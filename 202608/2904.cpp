class Solution {
public:
  string shortestBeautifulSubstring(string s, int k) {
    string_view ans;
    int len = s.size() + 1;
    size_t j = 0;
    for (size_t i = 0; i < s.size(); ++i) {
      if (s[i] == '1')
        --k;
      while (k < 0) {
        if (s[j++] == '1') {
          ++k;
        }
      }

      if (k == 0) {
        while (s[j] == '0') {
          ++j;
        }
        std::string_view sv{s.data() + j, i - j + 1};
        if (i - j + 1 < len || (i - j + 1 == len && sv < ans)) {
          ans = sv;
          len = i - j + 1;
        }
      }
    }
    return string(ans);
  }
};
