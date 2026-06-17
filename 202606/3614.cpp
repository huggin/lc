class Solution {
public:
  char processStr(string s, long long k) {
    long long n = 0;
    for (char c : s) {
      if (c == '#') {
        n += n;
      } else if (c == '%') {
        continue;
      } else if (c == '*') {
        if (n > 0) {
          --n;
        }
      } else {
        ++n;
      }
    }
    if (k >= n)
      return '.';
    for (char c : s | std::views::reverse) {
      if (c == '#') {
        n /= 2;
        k %= n;
      } else if (c == '%') {
        k = n - 1 - k;
      } else if (c == '*') {
        if (n >= 0) {
          ++n;
        }
      } else {
        if (k == n - 1)
          return c;
        --n;
      }
    }
    return '.';
  }
};
