class Solution {
public:
  bool sumGame(string num) {
    int cnt = count(begin(num), end(num), '?');
    if (cnt & 1)
      return true;
    int left = 0, right = 0, lc = 0, rc = 0;
    int n = num.size();
    for (int i = 0; i < n / 2; ++i) {
      if (num[i] == '?')
        ++lc;
      else
        left += num[i] - '0';
    }
    for (int i = n / 2; i < n; ++i) {
      if (num[i] == '?')
        ++rc;
      else
        right += num[i] - '0';
    }
    if (left > right && (left - right) != 9 * (rc - lc) / 2)
      return true;
    if (right > left && (right - left) != 9 * (lc - rc) / 2)
      return true;
    if (left == right && rc != lc)
      return true;
    return false;
  }
};
