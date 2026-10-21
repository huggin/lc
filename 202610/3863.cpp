class Solution {
public:
  int minOperations(string s) {
    if (is_sorted(begin(s), end(s)))
      return 0;
    auto [it1, it2] = minmax_element(begin(s), end(s));
    if (*it1 == s[0] || *it2 == s[s.size() - 1])
      return 1;
    if (*it1 == s[s.size() - 1] && *it2 == s[0]) {
      if (s.size() == 2)
        return -1;
      for (int i = 1; i < s.size() - 1; ++i) {
        if (s[i] == *it1 || s[i] == *it2)
          return 2;
      }
      return 3;
    }
    return 2;
  }
};
